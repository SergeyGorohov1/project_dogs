from django.urls import path
from dogs.views import index, breeds, dogs_breeds
from dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
    path("", index, name="index"),
    path("breeds/", breeds, name="breeds"),
    path("dogs/<int:pk>/", dogs_breeds, name="dogs_breeds"),
]