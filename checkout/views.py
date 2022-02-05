from django.shortcuts import render
from .forms import OrderForm
from .models import Order, OrderLineItem


def checkout(request):
    """
    View to handle checkout activities
    - renders template
    - form submission
    - stripe integration
    """

    # POST handler
    # get the order shipping details from form
    # get the order price details
    # handle stripe payment
    # create an order in the database
    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }
    return render(request, template, context)
