from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("patientlist", views.patientlist, name="patientlist"),
    path("showpatient/<str:id>/", views.showpatient, name="showpatient")
]