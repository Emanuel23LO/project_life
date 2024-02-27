from django.db import models
from django.utils import timezone


class Payment(models.Model):
    payment_method = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    value = models.FloatField(max_length=500)
    booking = models.ForeignKey('bookings.Booking', on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str.booking

    def save(self, *args, **kwargs):
     # Set date_booking only if it's not already set
        if not self.date_booking:
            self.date_booking = timezone.now()
        super().save(*args, **kwargs)








