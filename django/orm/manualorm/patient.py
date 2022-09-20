from django.db import connection

class Patient:
    def __init__(self, id):
        self.__id = id
        with connection.cursor() as cursor:
            cursor.execute("SELECT name, age, station_id FROM patient where id='" + id + "';")
            patient = cursor.fetchone()
            self.__name = patient[0]
            self.__age = patient[1]
            self.__stationid = patient[2]
    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_station_id(self):
        return self.__stationid