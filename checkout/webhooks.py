from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.forms import OrderForm

from .models import OrderLineItem, Order
from products.models import Shoe

import stripe
import json

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
    if event['type'] == 'payment_intent.succeeded':
        # line_items = event['line_items']
        intent = event['data']['object']
        try:
            fulfill_order(intent)
            return HttpResponse(
                content=
                f"Webhook recieved: {event['type']} | SUCCESS: Payment successful and order fulfilled in db",
                status=200)
        except Exception as e:
            return HttpResponse(
                content=
                f"Webhook recieved: {event['type']} | ERROR: Unsuccessful in saving order to db {e}",
                status=500)

    elif event['type'] == 'payment_intent.payment_failed':
        return HttpResponse(
            content=
            f"Webhook recieved: {event['type']} | ERROR: Payment was unsucessful - order not saved in db",
            status=500)

    return HttpResponse(status=200)


def fulfill_order(intent):
    cart = json.loads(intent.metadata.cart)
    order = Order(
        full_name=intent.shipping.name,
        phone_number=intent.shipping.phone,
        street1=intent.shipping.address.line1,
        street2=intent.shipping.address.line2,
        town_or_city=intent.shipping.address.city,
        county=intent.shipping.address.state,
        postcode=intent.shipping.address.postal_code,
        order_total=intent.metadata.order_total,
        delivery_cost=intent.metadata.delivery_cost,
        grand_total=intent.metadata.grand_total,
        stripe_pid=intent.id,
    )

    order.save()

    for shoe_id in cart:
        shoe_db = Shoe.objects.get(pk=shoe_id)
        for size in cart[shoe_id]:
            order_lineitem = OrderLineItem(
                order=order,
                shoe=shoe_db,
                size=size,
                qty=cart[shoe_id][size]['qty'],
            )
            order_lineitem.save()
