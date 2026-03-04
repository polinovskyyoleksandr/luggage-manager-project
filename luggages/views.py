from django.shortcuts import render
from django.http import HttpResponse
from .models import Flight

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def flight_index(request):
    flights = Flight.objects.all()
    return render(request, 'flights/index.html', {'flights':flights})