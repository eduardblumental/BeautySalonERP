from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()


class Device(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()


class Procedure(models.Model):
    name = models.CharField(max_length=50)
    required_device = models.ForeignKey(Device, on_delete=models.CASCADE)


class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    procedures = models.ForeignKey(Procedure, on_delete=models.SET_NULL)


class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()


class Appointment():
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, default=None, null=True, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
