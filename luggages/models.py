from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.

TYPES = (
    ('p', 'purse'),
    ('b', 'backpack'),
    ('c', 'carry-on luggage'),
    ('s', 'suitcase'),
    ('br', 'briefcase')
)

SIZES = (
    ('s', 'small'),
    ('m', 'medium'),
    ('l', 'large')
)

class Flight(models.Model):
    flight_number = models.CharField(max_length=6)
    destination = models.CharField(max_length=20, null=True, blank=True)
    departure_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.destination} - {self.flight_number} : from:({self.departure_date}) - to:({self.return_date})"
    
    def get_absolute_url(self):
        return reverse('flight-detail', kwargs={'flight_id': self.id})
    
class Luggage(models.Model):
    type=models.CharField(max_length=50, choices=TYPES, default=TYPES[2][0])
    size=models.CharField(max_length=50, choices=SIZES, default=TYPES[1][0])
    color=models.CharField(max_length=20)
    items=models.TextField(max_length=500, null=True, blank=True)

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} - {self.get_size_display()} - {self.color}"
