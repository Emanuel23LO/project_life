from django.db import models

class Booking_service(models.Model):
    value = models.FloatField(max_length=200)
    status = models.BooleanField(default=True)
    

def __str__(self):
    return self.name