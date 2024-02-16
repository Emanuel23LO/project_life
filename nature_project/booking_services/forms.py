from django import forms
from . models import Booking_service
from bookings.models import Booking
from services.models import Service

class Booking_serviceForm(forms.ModelForm):
    booking = forms.ModelChoiceField(queryset=Booking.objects.filter(status=True).order_by('value'))
    service = forms.ModelChoiceField(queryset=Service.objects.filter(status=True).order_by('name'))
    class Meta:
        model = Booking_service
        fields = "__all__"
        exclude = ['status']
        labels = {
            'value': 'Valor',                   
        }
        widgets = {
            'value': forms.NumberInput(attrs={'placeholder': 'Ingresa el valor'}),
        }