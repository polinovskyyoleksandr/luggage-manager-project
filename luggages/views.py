from django.shortcuts import render, redirect
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Flight
from .forms import FlightForm, LuggageForm
from django.contrib.auth.views import LoginView

# Create your views here.

class Home(LoginView):
    template_name = 'home.html'
    
def about(request):
    return render(request, 'about.html')

@login_required
def flight_index(request):
    print("flight_index called, user:", request.user)
    flights = Flight.objects.filter(user=request.user)
    print("Flights queryset:", flights)
    return render(request, 'flights/index.html', {'flights':flights})

@login_required
def flight_detail(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    luggage_form = LuggageForm()
    return render(request, 'flights/detail.html', {'flight': flight, 'luggage_form': luggage_form})

class FlightCreate(LoginRequiredMixin, CreateView):
    model = Flight
    form_class = FlightForm
    template_name = 'luggages/flight_form.html'
    def form_valid(self, form):
        print("Current user:", self.request.user)
        form.instance.user = self.request.user
        return super().form_valid(form)

class FlightUpdate(LoginRequiredMixin, UpdateView):
    model = Flight
    fields = ['destination', 'departure_date', 'return_date']

class FlightDelete(LoginRequiredMixin, DeleteView):
    model = Flight
    success_url='/flights/'

@login_required
def add_luggage(request, flight_id):
    form = LuggageForm(request.POST)
    if form.is_valid():
        new_luggage = form.save(commit=False)
        new_luggage.flight_id = flight_id
        new_luggage.save()
    return redirect('flight-detail', flight_id = flight_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('flight-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

