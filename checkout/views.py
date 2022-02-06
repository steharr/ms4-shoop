from django.shortcuts import render, redirect
from django.urls import reverse

from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem

import json
import stripe
import os

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
    # get current domain
    host = request.get_host()
    if request.method == 'POST':

        # create a checkout session (page hosted by stripe)
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'eur',
                            'unit_amount': 200,
                            'product_data': {
                                'name': 'test',
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url="http://{}{}".format(host,
                                                 reverse('payment_success')),
                cancel_url="http://{}{}".format(host,
                                                reverse('payment_cancel')),
            )
        except Exception as e:
            return str(e)

    return redirect(checkout_session.url, code=303)


def payment_success(request):
    context = {'payment_status': 'success'}
    return render(request, 'checkout/confirmation.html', context)


def payment_cancel(request):
    context = {'payment_status': 'cancel'}
    return render(request, 'checkout/confirmation.html', context)
