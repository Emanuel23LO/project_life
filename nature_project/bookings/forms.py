from django import forms
from .models import Booking
from customers.models import Customer

class BookingForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.filter(status=True).order_by('name'))
    status = forms.TypedChoiceField(
        choices=Booking.status_choices,
        coerce=int,
        initial=1  # Esto establece el valor inicial
    )

    class Meta:
        model = Booking
        fields = "__all__"
        labels = {
            'reservation_date': 'Fecha de reservacion',
            'start_date': 'Fecha inicio',
            'end_date': 'Fecha fin', 
            'value': 'valor',    
            'customer': 'cliente',   
            'status': 'Estado',                        
        }
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),   
            'value': forms.NumberInput(attrs={'placeholder': 'Ingresa el valor'}),    
            'status': forms.Select(),
        }
