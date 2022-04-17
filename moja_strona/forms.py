from django import forms
from .models import Order, Opinion

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name',
            'email',
            'adress',
            'delivery',
            'info_product',

        ]

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = [
            'name',
            # 'email',
            'opinion',
        ]