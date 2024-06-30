from django.shortcuts import render, redirect

from .forms import FlightsForm
from .models import Flight
# Create your views here.

def index(request):
    return render(request, "index.html")

def flights(request):
    if request.method == "POST" and request.user.is_authenticated:
        form = FlightsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.user = request.user
            flight.image = form.cleaned_data['image']
            flight.save()

    form = FlightsForm()

    flights = Flight.objects.filter(takeoff_airport="Skopje").all()

    return render(request, "flights.html", context={"form": form, "flights" : flights})

def edit_flight(request, id):
    flight_instance = Flight.objects.filter(id=id).first()
    if request.method == "POST":
        flight = FlightsForm(request.POST, instance=flight_instance)
        if flight.is_valid():
            flight.save()
        return redirect("flights")
    else:
        flight = FlightsForm(instance=flight_instance)

    return render(request, "edit_flight.html", {"form": flight})

def delete_flight(request, id):
    flight_instance = Flight.objects.filter(id=id).get()
    if request.method == "POST":
        flight_instance.delete()
        return redirect("flights")

    return render(request, "delete_flight.html")