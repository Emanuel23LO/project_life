from django.shortcuts import render, redirect
from payments.models import Payment
from django.http import JsonResponse
from django.contrib import messages



from .forms import PaymentForm
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
    payment = Payment.objects.get(pk=payment_id)
    data = { 'payment_method': payment.payment_method, 'date': payment.date, 'value': payment.value }
    return JsonResponse(data)

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