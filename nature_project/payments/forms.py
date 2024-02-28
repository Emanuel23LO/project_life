from django import forms
from . models import Payment
from bookings.models import Booking


class PaymentForm(forms.ModelForm):
    booking = forms.ModelChoiceField(queryset= Booking.objects.filter().order_by('id'), label='Cliente')
    class Meta:
        model = Payment
        fields = "__all__"
        exclude = ['status']
        labels = {
            'payment_method': 'Metodo de pago',
            'date': 'Fecha ',
            'value': 'Valor',   
            'booking': 'Cliente' 
        }
        widgets = {
            'payment_method': forms.TextInput(attrs={'placeholder': 'Ingresa metodo de pago'}),      
            'date': forms.DateInput(attrs={'type': 'date'}),   
            'value': forms.TextInput(attrs={'placeholder': 'Ingresa el valor'}),             
        }