from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'full_name', 'email', 'phone_number', 'street1', 'street2',
            'town_or_city', 'postcode', 'country', 'county'
        ]
