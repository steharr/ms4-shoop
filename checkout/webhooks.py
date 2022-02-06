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

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Passed signature verification
    return HttpResponse(status=200)
