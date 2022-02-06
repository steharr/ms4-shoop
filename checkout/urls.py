from django.contrib import admin
from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('preview/', views.checkout_preview, name='checkout_preview'),
    path('create-checkout-session/',
         views.create_checkout_session,
         name='create_checkout_session'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancel/', views.payment_cancel, name='payment_cancel'),
    path('wh/', webhook, name='webhook'),
]
