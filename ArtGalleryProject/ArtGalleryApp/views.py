from datetime import datetime

from django.shortcuts import render, redirect
from .models import ArtExhibition
from .forms import ArtExhibitionForm


# Create your views here.


def index(request):
    all_exhibitions = ArtExhibition.objects.all()

    return render(request, "exhibitions.html", {"exhibitions": all_exhibitions})


def add(request):
    form = ArtExhibitionForm()
    future_exhibitions = ArtExhibition.objects.filter(from_date__gte=datetime.now().date()).all()
    context = {'form': form, 'future_exhibitions': future_exhibitions}

    if request.method == "POST":
        exhibition_form = ArtExhibitionForm(request.POST, files=request.FILES)

        if exhibition_form.is_valid():
            exhibition = exhibition_form.save()

        return redirect("index")

    return render(request, 'add_exhibition.html', context=context)
