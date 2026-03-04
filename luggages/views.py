from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Flight

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
    return render(request, 'flights/detail.html', {'flight': flight})

class FlightCreate(CreateView):
    model = Flight
    fields = '__all__'

class FlightUpdate(UpdateView):
    model = Flight
    fields = '__all__'

class FlightDelete(DeleteView):
    model = Flight
    success_url='/flights/'