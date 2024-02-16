from django.db import models

class Booking(models.Model):
    reservation_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    value = models.FloatField(max_length=50)
    customer = models.ForeignKey('customers.Customer', on_delete=models.DO_NOTHING)
    status_choices = [
        (1, 'Reservado'),
        (2, 'Por Confirmar'),
        (3, 'Confirmado'),
        (4, 'En Ejecucion'),
        (5, 'Anulada'),
    ]
    status = models.PositiveSmallIntegerField(
        choices = status_choices,
        default =1
    )

    def __str__(self):
        return f"{self.customer.name} - {self.get_status_display()}"

