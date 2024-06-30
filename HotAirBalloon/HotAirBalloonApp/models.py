from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class HotAirBalloon(models.Model):
    TYPE_CHOICES = [
        ("Montgolfier", "Montgolfier"),
        ("Sky Lanterns", "Sky Lanterns"),
        ("Tourism", "Tourism"),
        ("Racing", "Racing"),
        ("Observation", "Observation"),
        ("Novelty", "Novelty"),
        ("Advertising", "Advertising")
    ]

    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    manufacturer = models.CharField(max_length=30)
    capacity = models.IntegerField()

    def __str__(self):
        return self.manufacturer


class Airline(models.Model):
    name = models.CharField(max_length=30)
    year_of_establishment = models.DateField()
    is_international = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Pilot(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_date = models.DateField(auto_now=True)
    experience = models.IntegerField()
    rank = models.CharField(max_length=30)

    def __str__(self):
        return self.name + " " + self.surname


class AirlinePilot(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)


class Flight(models.Model):
    code = models.CharField(max_length=10)
    takeoff_airport = models.CharField(max_length=50)
    landing_airport = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='flight_images/', blank=True, null=True)
    hot_air_balloon = models.ForeignKey(HotAirBalloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
