from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    document = models.IntegerField(unique=True)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=300)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
