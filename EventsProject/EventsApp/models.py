from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Band(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    year = models.IntegerField()
    number_of_events = models.IntegerField()

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    poster = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    bands = models.CharField(max_length=255, null=True,blank=True)
    is_open = models.BooleanField()

    def __str__(self):
        return self.name


class BandEvent(models.Model):
    band = models.ForeignKey(Band,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name + " " + self.band.name