from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Manufacturer (models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    origin = models.CharField(max_length=50)
    ceo = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car (models.Model):
    CAR_CHOICES = [
        ("sedan", "Sedan"),
        ("hatchback", "Hatchback"),
        ("cabriolet", "Cabriolet"),
        ("wagon", "Wagon"),
        ("coupe", "Coupe"),
        ("oldtimer", "Old Timer")
    ]

    type = models.CharField(max_length= 10, choices=CAR_CHOICES)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    paint = models.CharField(max_length=30)
    isOldTimer = models.BooleanField()

    def __str__(self):
        return self.manufacturer.name + " " + self.type

class WorkShop (models.Model):
    name = models.CharField(max_length=30)
    year_started = models.IntegerField()
    repairs_oldtimers = models.BooleanField()

    def __str__(self):
        return self.name

class Repair (models.Model):
    code = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to="repairs/", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    workshop = models.ForeignKey(WorkShop, on_delete=models.CASCADE)

    def __str__(self):
        return self.code + " - " + self.car.manufacturer.name + " " + self.car.type

class ManufacturerWorkshop(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    workshop = models.ForeignKey(WorkShop, on_delete=models.CASCADE)

    def __str__(self):
        return self.manufacturer.name + " - " + self.workshop.name