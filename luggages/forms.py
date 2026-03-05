from django import forms
from .models import Flight, Luggage

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_number', 'destination', 'departure_date', 'return_date']
        widgets = {
            'departure_date': forms.DateInput(
                format='%d-%m-%Y',
                attrs={'placeholder': 'Select a date', 'type': 'date'}
            ),
            'return_date': forms.DateInput(
                format='%d-%m-%Y',
                attrs={'placeholder': 'Select a date', 'type': 'date'}
            )
        }

class LuggageForm(forms.ModelForm):
    class Meta:
        model = Luggage
        fields = ['type', 'size', 'color', 'items']
