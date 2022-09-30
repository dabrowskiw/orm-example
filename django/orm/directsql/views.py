from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def index(request):
    with connection.cursor() as cursor:
        response = ["<b>Stations:</b><ul>"]
        cursor.execute("SELECT id, name FROM station;")
        for station in cursor.fetchall():
            response += ['<li><a href="showstation/' + str(station[0]) + '">' + station[1] + '</a>'] 
        response += ["</ul>"]
        response += ["<b>Patients:</b><ul>"]
        cursor.execute("SELECT id, name FROM patient;")
        for patient in cursor.fetchall():
            response += ['<li><a href="showpatient/' + str(patient[0]) + '">' + patient[1] + '</a>'] 
        response += ["</ul>"]
        return HttpResponse("".join(response))

def showstation(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name, capacity FROM station WHERE id='" + str(id) + "';")
        station = cursor.fetchone()
        response = ["<html><b>Name:</b> {name}<br><b>Capacity:</b> {capacity}<br><b>Patients:</b><ul>".format(name=station[1], capacity=station[2])]
        cursor.execute("SELECT id, name FROM patient where station_id='" + str(station[0]) + "';")
        for patient in cursor.fetchall():
            response += ['<li><a href="../../showpatient/' + str(patient[0]) + '/">' + patient[1] + "</a>"]
    response += ["</ul></li>"]
    return HttpResponse("".join(response))


def showpatient(request, id):
    response = "<b>Name:</b> {name}<br><b>Age:</b> {age}<br><b>Station:</b> {station}"
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, age, station_id FROM patient where id='" + id + "';")
        patient = cursor.fetchone()
        cursor.execute("SELECT id, name FROM station WHERE id='" + str(patient[2]) + "';")
        station = cursor.fetchone()
        stationlink = ""
        if station is not None:
            stationlink = '<a href="../../showstation/' + str(station[0]) + '">' + station[1] + "</a>"
        return HttpResponse(response.format(name=patient[0], age=patient[1], station=stationlink))

