from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def index(request):
    return HttpResponse("Hello, world!")

def patientlist(request):
    response = ["<HTML><TABLE><TR><TH>Patient name</TH><TH>Patient age</TH></TR>"]
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, age FROM patient;")
        for row in cursor.fetchall():
            response += ["<TR><TD>", row[0], "</TD><TD>", str(row[1]), "</TD></TR>"]
    response += ["</TABLE></HTML>"]
    return HttpResponse("".join(response))

def showpatient(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, age, station_id FROM patient where id='" + id + "';")
        patient = cursor.fetchone()
        response = "<b>Name:</b> {name}<br><b>Age:</b> {age}<br><b>Station:</b> {station}"
        return HttpResponse(response.format(name=patient[0], age=patient[1], station=patient[2]))

