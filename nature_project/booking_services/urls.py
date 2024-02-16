from . import views
from django.urls import path

urlpatterns = [      
    path('', views.booking_services, name='booking_services'),
    path('booking_service_status_/<int:booking_service_id>/', views.change_status_booking_service, name='booking_service_status'), 
    path('create/', views.create_booking_service, name='create_booking_service'),                
]