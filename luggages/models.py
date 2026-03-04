from django.db import models
from django.urls import reverse

# Create your models here.

class Flight(models.Model):
    flight_number = models.CharField(max_length=6)
    departure_date = models.DateField
    return_date = models.DateField

    def __str__(self):
        return self.flight_number
    
    def get_absolute_url(self):
        return reverse('flight-detail', kwargs={'flight_id': self.id})