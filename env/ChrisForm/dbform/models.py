from django.db import models

# Create your models here.

class Volunteer(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Email = models.CharField(max_length=50)

class Job(models.Model):
    Volunteer = models.CharField(max_length=100)
    Client = models.CharField(max_length=100)
    Date = models.DateField(blank=True, null=True)
    Summary = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)

class Client(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Email = models.CharField(max_length=100)
    Notes = models.CharField(max_length=255)