from django.shortcuts import render, redirect

from hotel_app.forms import ReservationForm
from hotel_app.models import Room, Reservation


# Create your views here.

def index(request):

    rooms = Room.objects.filter(is_clean=True, beds__lt=5).all()
    return render(request, 'index.html', {"rooms": rooms})

def reservations(request):

    reservations = Reservation.objects.all()
    return render(request, 'reservations.html', {"reservations": reservations})

def add_reservation(request):
    form = ReservationForm()
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST, files= request.FILES)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.user = request.user
            reservation.id_picture = reservation_form.cleaned_data['id_picture']
            reservation.save()
        return redirect("index")

    return render(request, 'add_reservation.html', {"form": form})

def details_reservation(request, id):
    reservation = Reservation.objects.filter(id=id).get()
    return render(request, "details_reservation.html", {"reservation" : reservation})