from django import forms
from .models import Car
from tempus_dominus.widgets import DateTimePicker

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'brand', 'price', 'is_bought', 'buyer', 'buy_time']

