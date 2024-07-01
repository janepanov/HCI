from datetime import datetime

from django.shortcuts import render,redirect

from EventsApp.forms import EventForm
from EventsApp.models import Event, Band, BandEvent


# Create your views here.

def index(request):
    events = Event.objects.filter(date__lte=datetime.now().date()).all()

    return render(request, 'index.html', {"events": events})


def addEvent(request):
    form = EventForm()
    if request.method == 'POST':
        event_form = EventForm(request.POST, files=request.FILES)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.user = request.user
            event.save()
            event.poster = event_form.cleaned_data['poster']
            bands = event_form.cleaned_data['bands']
            bands_list = bands.split(',')
            for band in bands_list:
                band_obj = Band.objects.filter(name=band).first()
                if band_obj:
                    band_obj.number_of_events = band_obj.number_of_events + 1
                    band_obj.save()
                    BandEvent.objects.create(band=band_obj, event=event)
            return redirect("index")
    return render(request, "add-event.html", {"form": form})
