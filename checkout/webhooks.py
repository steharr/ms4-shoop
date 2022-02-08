from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from products.models import Shoe
from .models import Order, OrderLineItem

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
wh_secret = settings.STRIPE_WEBHOOK_SECRET


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listens to webhooks from stripe
    """
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    # verify event came from stripe
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        # Unknown exception
        return HttpResponse(content=e, status=400)

    # If no exception, passed signature verification
    print("WEBHOOK EVENT --> " + event['type'])

    # Handle the event coming from the checkout
    if event['type'] == 'payment_intent.created':
        intent = event['data']['object']
        append_payment_intent_to_order(intent)
        return HttpResponse(
            content=
            f"Webhook recieved: {event['type']} | SUCCESS: Payment Intent Created",
            status=200)

    elif event['type'] == 'payment_intent.suceeded':
        intent = event['data']['object']
        try:
            update_order_status_payment(intent)
            return HttpResponse(
                content=
                f"Webhook recieved: {event['type']} | SUCCESS: Order status updated",
                status=200)
        except Exception as e:
            return HttpResponse(
                content=
                f"Webhook recieved: {event['type']} | ERROR: Unsuccesful in updating order status due to {e}",
                status=500)

    elif event['type'] == 'payment_intent.payment_failed':
        return HttpResponse(
            content=
            f"Webhook recieved: {event['type']} | ERROR: Payment was unsucessful",
            status=500)

    return HttpResponse(status=200)


def update_order_status_payment(intent):

    # extract the order id from the intent
    order_id = intent.metadata.order
    order = Order.objects.get(pk=order_id)

    # update the order status to payment recieved
    if order.order_status == 'A':
        order.order_status = 'B'

    # save the order with the new order status
    order.save()


def append_payment_intent_to_order(intent):

    # extract the order id from the intent
    order_id = intent.metadata.order
    order = Order.objects.get(pk=order_id)

    # add the payment intent id to order in the database
    payement_intent_id = intent.id
    order.pid = payement_intent_id

    # save the order with the pid
    order.save()