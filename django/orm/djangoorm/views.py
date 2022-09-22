from django.shortcuts import render
from django.http import HttpResponse
from djangoorm.models import Patient, Station

def index(request):
    response = ["<b>Stations:</b><ul>"]
    for station in Station.objects.all():
        response += ['<li><a href="showstation/' + str(station.id) + '">' + station.name + '</a>'] 
    response += ["</ul>"]
    response += ["<b>Patients:</b><ul>"]
    for patient in Patient.objects.all():
        response += ['<li><a href="showpatient/' + str(patient.id) + '">' + patient.name + '</a>'] 
    response += ["</ul>"]
    return HttpResponse("".join(response))
    
def showpatient(request, id):
    patient = Patient.objects.all().filter(id=id).first()
    response = "<b>Name:</b> {name}<br><b>Age:</b> {age}<br><b>Station:</b> {station}"
    station = patient.station
    stationlink = '<a href="../../showstation/' + str(station.id) + '">' + station.name + "</a>"
    return HttpResponse(response.format(name=patient.name, age=patient.age, station=stationlink))

def showstation(request, id):
    station = Station.objects.get(id=id)
    response = ["<html><b>Name:</b> {name}<br><b>Capacity:</b> {capacity}<br><b>Patients:</b><ul>".format(name=station.name, capacity=station.capacity)]
    for patient in station.patient_set.all():
        response += ['<li><a href="../../showpatient/' + str(patient.id) + '/">' + patient.name + "</a>"]
    response += ["</ul></li>"]
    return HttpResponse("".join(response))

