from django.db import models
from django.forms import JSONField

# Create your models here.
class Booking(models.Model):   
    date_booking = models.DateTimeField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    value = models.IntegerField()
    
    reserved = 'Reservado'
    running = 'En ejecucion' 
    finalize = 'Finalizado'
    cancele = 'Anulado'
    status = models.CharField(
        max_length=20, 
        choices=[
            (reserved, 'Reservado'), 
            (running, 'Ejecución'),
            (finalize, 'Finalizado'),
            (cancele, 'Anulado'),
        ],
        default=reserved
    )  
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.value)
    

