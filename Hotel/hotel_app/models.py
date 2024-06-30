from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Room(models.Model):
    room_number = models.IntegerField()
    beds = models.IntegerField()
    has_terrace = models.BooleanField()
    is_clean = models.BooleanField()

    def __str__(self):
        return str(self.room_number)


class Employee(models.Model):
    EMPLOYEE_CHOICES = (
        ('H', 'H'),
        ('R', 'R'),
        ('M', 'M')
    )
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    work_description = models.TextField()
    employment_year = models.IntegerField()
    employee_type = models.CharField(max_length=30, choices=EMPLOYEE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class RoomEmployee(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Reservation(models.Model):
    code = models.CharField(max_length=30)
    from_date = models.DateField()
    to_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    id_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    is_confirmed = models.BooleanField()
    confirmed_by = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} {self.room.room_number}"
