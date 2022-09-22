from django.shortcuts import render
from django.http import HttpResponse
from .ormmodels import Patient, Station

def index(request):
    response = ["<b>Stations:</b><ul>"]
    for station in Station.get_all_stations():
        response += ['<li><a href="showstation/' + str(station.id) + '">' + station.name + '</a>'] 
    response += ["</ul>"]
    response += ["<b>Patients:</b><ul>"]
    for patient in Patient.get_all_patients():
        response += ['<li><a href="showpatient/' + str(patient.id) + '">' + patient.name + '</a>'] 
    response += ["</ul>"]
    return HttpResponse("".join(response))

def showpatient(request, id):
    patient = Patient(id)
    response = "<b>Name:</b> {name}<br><b>Age:</b> {age}<br><b>Station:</b> {station}"
    station = patient.get_station()
    stationlink = '<a href="../../showstation/' + str(station.id) + '">' + station.name + "</a>"
    return HttpResponse(response.format(name=patient.name, age=patient.age, station=stationlink))

def showstation(request, id):
    station = Station(id)
    response = ["<html><b>Name:</b> {name}<br><b>Capacity:</b> {capacity}<br><b>Patients:</b><ul>".format(name=station.name, capacity=station.capacity)]
    for patient in station.get_patients():
        response += ['<li><a href="../../showpatient/' + str(patient.id) + '/">' + patient.name + "</a>"]
    response += ["</ul></li>"]
    return HttpResponse("".join(response))
