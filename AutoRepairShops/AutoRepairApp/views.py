from django.shortcuts import render, redirect

from .forms import RepairsForm
from .models import Repair, Car

# Create your views here.

def index(request):
    return render(request, "index.html")

def repairs(request):
    if request.method == "POST":
        form = RepairsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.user = request.user
            repair.image = form.cleaned_data['image']
            repair.save()

    form = RepairsForm()

    repairs = Repair.objects.filter(user=request.user, car__type="sedan").all()

    return render(request, "repairs.html", context={"form": form, "repairs" : repairs})