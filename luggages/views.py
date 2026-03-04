from django.shortcuts import render, redirect
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Flight
from .forms import FlightForm, LuggageForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def flight_index(request):
    flights = Flight.objects.all()
    return render(request, 'flights/index.html', {'flights':flights})

def flight_detail(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    luggage_form = LuggageForm()
    return render(request, 'flights/detail.html', {'flight': flight, 'luggage_form': luggage_form})

class FlightCreate(CreateView):
    model = Flight
    form_class = FlightForm
    template_name = 'luggages/flight_form.html'


class FlightUpdate(UpdateView):
    model = Flight
    fields = '__all__'

class FlightDelete(DeleteView):
    model = Flight
    success_url='/flights/'

def add_luggage(request, flight_id):
    form = LuggageForm(request.POST)
    if form.is_valid():
        new_luggage = form.save(commit=False)
        new_luggage.flight_id = flight_id
        new_luggage.save()
    return redirect('flight-detail', flight_id = flight_id)
