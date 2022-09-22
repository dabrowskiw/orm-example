from django.db import models

class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    station = models.ForeignKey("Station", models.PROTECT)

class Station(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    capacity = models.IntegerField()


# Create your models here.
