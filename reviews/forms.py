from django import forms
from .models import Review
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Disables user and shoe fields
        """
        super().__init__(*args, **kwargs)
        self.fields['shoe'].widget = forms.HiddenInput()
        self.fields['user'].widget = forms.HiddenInput()