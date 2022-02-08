from django.shortcuts import render, redirect
from django.urls import reverse

from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Shoe

import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout_preview(request):
    """ 
    Shows order summary &
    provides form for delivery details
    """
    order_form = OrderForm()
    template = 'checkout/checkout_preview.html'
    context = {
        'order_form': order_form,
    }
    return render(request, template, context)


def create_checkout_session(request):
    # get the users session cart
    cart = request.session.get('cart', {})
    # get current domain
    host = request.get_host()

    if request.method == 'POST':
        # extract order details
        order_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street1': request.POST['street1'],
            'street2': request.POST['street2'],
            'county': request.POST['county'],
            'order_total': request.POST['order_total'],
            'delivery_cost': request.POST['delivery_cost'],
            'grand_total': request.POST['grand_total'],
        }

        order_form = OrderForm(order_data)
        if order_form.is_valid():  # validate the information given
            cart_line_items = []
            for shoe_id in cart:
                for size in cart[shoe_id]:
                    shoe = Shoe.objects.get(pk=shoe_id)
                    cart_line_items.append({
                        'price_data': {
                            'currency': 'eur',
                            'unit_amount': int(shoe.price * 100),
                            'product_data': {
                                'name': shoe.name + " - Size: " + size,
                            },
                        },
                        'quantity':
                        int(cart[shoe_id][size]['qty']),
                    })

            # create a checkout session (page hosted by stripe)
            try:
                checkout_session = stripe.checkout.Session.create(
                    # customer email
                    customer_email=order_data['email'],
                    # payment method
                    payment_method_types=['card'],
                    # order line items for payment page
                    line_items=cart_line_items,
                    mode='payment',
                    # order details for order fulfillment
                    payment_intent_data={
                        'shipping': {
                            'name': order_data['full_name'],
                            'phone': order_data['phone_number'],
                            'address': {
                                'line1': order_data['street1'],
                                'line2': order_data['street2'],
                                'city': order_data['town_or_city'],
                                'country': order_data['country'],
                                'postal_code': order_data['postcode'],
                                'state': order_data['county'],
                            }
                        },
                        'metadata': {
                            'order_total': order_data['order_total'],
                            'delivery_cost': order_data['delivery_cost'],
                            'grand_total': order_data['grand_total'],
                            'cart': json.dumps(cart),
                        },
                    },
                    success_url="http://{}{}".format(
                        host, reverse('payment_success')),
                    cancel_url="http://{}{}".format(host,
                                                    reverse('payment_cancel')),
                )
            except Exception as e:
                return str(e)

            # redirect to the outcome page of the checkout session
            return redirect(checkout_session.url, code=303)

    return redirect(reverse('checkout'))


def payment_success(request):

    orders = OrderLineItem.objects.all
    context = {'payment_status': 'success', 'orders': orders}
    return render(request, 'checkout/confirmation.html', context)


def payment_cancel(request):
    # payment was cancelled so need to delete order in the database
    context = {'payment_status': 'cancel'}
    return render(request, 'checkout/confirmation.html', context)
