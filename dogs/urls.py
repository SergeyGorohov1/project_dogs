from django.urls import path
from dogs.views import index, BreedView, DogView
from dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
    path("", index, name="index"),
    path("breeds/", BreedView.as_view(), name="breeds"),
    path("dogs/<int:pk>/", DogView.as_view(), name="dogs_breeds"),
]