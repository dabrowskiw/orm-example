from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("showstation/<str:id>/", views.showstation, name="showstation"),
    path("showpatient/<str:id>/", views.showpatient, name="showpatient"),
]