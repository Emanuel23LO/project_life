from django.shortcuts import render, redirect
from payments.models import Payment
from django.http import JsonResponse
from django.contrib import messages
from .forms import PaymentForm
from bookings.models import Booking




def status_payment(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    payment = Payment.objects.filter(booking=booking).first()

    
    if payment.value >= 0.5 * booking.value:
        estado = booking.reserved
    elif payment.value == booking.value:
            estado = booking.running
    else:
        estado = 'esta mal el codigo'

    return render(request, 'payment/index.html', {'estado': estado})
    
def payments(request):    
    payments_list = Payment.objects.all()    
    return render(request, 'payments/index.html', {'payments_list': payments_list})

def change_status_payment(request, payment_id):
    payment = Payment.objects.get(pk=payment_id)
    payment.status = not payment.status
    payment.save()
    return redirect('payments')

def create_payment(request):
    form = PaymentForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Pago creado correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al crear el pago.')
        return redirect('payments')    
    return render(request, 'payments/create.html', {'form': form})

def detail_payment(request, payment_id):
    try:
        payment = Payment.objects.get(pk=payment_id)
        data = {
            'payment_method': payment.payment_method,
            'date': payment.date,
            'value': payment.value,
        }
        return JsonResponse(data)
    except Payment.DoesNotExist:
        messages.error(request, 'El pago especificado no existe.')
        return JsonResponse({'error': 'Payment not found'}, status=404)
    except Exception as e:
        messages.error(request, f'Ocurrió un error al obtener los detalles del pago: {str(e)}')
        return JsonResponse({'error': str(e)}, status=500)

def delete_payment(request, payment_id):
    payment = Payment.objects.get(pk=payment_id)
    try:
        payment.delete()
        messages.success(request, 'Pago eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el pago porque está asociado a una reserva.')
    return redirect('payments')

def edit_payment(request, payment_id):
    payment = Payment.objects.get(pk=payment_id)
    form = PaymentForm(request.POST or None, request.FILES or None, instance=payment)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Pago actualizado correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al editar el pago.')
        return redirect('payments')    
    return render(request, 'payments/editar.html', {'form': form})