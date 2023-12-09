from django.urls import path
from dogs.views import index, BreedView, DogView, DogCreateView, DogDetailView, DogUpdateView, DogDeleteView
from dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
    path("", index, name="index"),
    path("breeds/", BreedView.as_view(), name="breeds"),
    path("dogs/<int:pk>/", DogView.as_view(), name="dogs_breeds"),
    path("dogs/view/<int:pk>/", DogDetailView.as_view(), name="dogs_view"),
    path("dogs/create/", DogCreateView.as_view(), name="dogs_create"),
    path("dogs/update/<int:pk>/", DogUpdateView.as_view(), name="dogs_update"),
    path("dogs/delete/<int:pk>/", DogDeleteView.as_view(), name="dogs_delete"),
]