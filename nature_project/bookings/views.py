from django.shortcuts import get_object_or_404, render, redirect

from bookings.models import Booking

from .forms import BookingForm

from django.http import JsonResponse

from django.contrib import messages

def bookings(request):    
    bookings_list = Booking.objects.all()    
    return render(request, 'bookings/index.html', {'bookings_list': bookings_list})

def change_status_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    
    # Obtén el próximo estado según tu lógica de elección
    next_status = booking.status + 1 if booking.status < len(Booking.status_choices) else 1
    
    booking.status = next_status
    booking.save()
    
    return redirect('bookings')



def create_booking(request):
    form = BookingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('bookings')    
    return render(request, 'bookings/create.html', {'form': form})

def detail_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    data = { 'reservation_date': booking.reservation_date, 'start_date': booking.start_date, 'end_date': booking.end_date, 'value': booking.value, 'customer': str(booking.customer) }    
    return JsonResponse(data)


def delete_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    try:
        booking.delete()        
        messages.success(request, 'Reserva eliminada correctamente.')
    except:
        messages.error(request, 'No se puede eliminar la reserva porque está asociado a otra tabla.')
    return redirect('bookings')