from django import forms
from .models import Banner


class BannerForm(forms.ModelForm):

    class Meta:
        model = Banner
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs[
            'placeholder'] = 'e.g. Christmas Sale'
        self.fields['price_threshold'].widget.attrs['placeholder'] = (
            'min value needed'
            'in order to be eligible for discount')
        self.fields['discount'].widget.attrs['min'] = 0
        self.fields['discount'].widget.attrs['max'] = 30
        self.fields['price_threshold'].widget.attrs['min'] = 0.00
        self.fields['price_threshold'].widget.attrs['max'] = 999.00
