from django.shortcuts import render, redirect

from booking_services.models import Booking_service

from .forms import Booking_serviceForm

def booking_services(request):    
    booking_services_list = Booking_service.objects.all()    
    return render(request, 'booking_services/index.html', {'booking_services_list': booking_services_list})

def change_status_booking_service(request, booking_service_id):
    booking_service = Booking_service.objects.get(pk=booking_service_id)
    booking_service.status = not booking_service.status
    booking_service.save()
    return redirect('booking_services')

def create_booking_service(request):
    form = Booking_serviceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('booking_services')    
    return render(request, 'booking_services/create.html', {'form': form})