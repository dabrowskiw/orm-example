from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .patient import Patient

def index(request):
    return HttpResponse("Hello, world!")

def showpatient(request, id):
    patient = Patient(id)
    response = "<b>Name:</b> {name}<br><b>Age:</b> {age}<br><b>Station:</b> {station}"
    return HttpResponse(response.format(name=patient.get_name(), age=patient.get_age(), station=patient.get_station_id()))

