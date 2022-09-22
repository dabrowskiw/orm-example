from django.db import connection

class Patient:
    def __init__(self, id):
        self.id = id
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM patient where id='" + str(id) + "';")
            patient = cursor.fetchone()
            self.name = patient[1]
            self.age = patient[2]
            self.station_id = patient[3]
    
    def get_station(self):
        return Station(self.station_id)

    def get_all_patients():
        res = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM patient")
            for patient in cursor.fetchall():
                res += [Patient(patient[0])]
        return res

    
class Station:
    def __init__(self, id):
        self.id = id
        with connection.cursor() as cursor:
            cursor.execute("SELECT name, capacity FROM station WHERE id='" + str(id) + "';")
            station = cursor.fetchone()
            self.name = station[0]
            self.capacity = station[1]
            self.patient_ids = []
            cursor.execute("SELECT id FROM patient WHERE station_id='" + str(id) + "';")
            for patient in cursor.fetchall():
                self.patient_ids += [patient[0]]
    
    def get_patients(self):
        res = []
        for id in self.patient_ids:
            res += [Patient(id)]
        return res

    def get_all_stations():
        res = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM station")
            for station in cursor.fetchall():
                res += [Station(station[0])]
        return res

