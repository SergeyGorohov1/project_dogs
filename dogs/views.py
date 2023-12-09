from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from dogs.models import Dog, Breed


def index(request):
    context = {
        "object_list": Breed.objects.all()[:3]
    }
    return render(request, "dogs/breed_list.html", context)


class BreedView(ListView):
    model = Breed


class DogView(ListView):
    model = Dog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(breed__pk=self.kwargs.get("pk"))
        return queryset


class DogDetailView(DetailView):
    model = Dog


class DogCreateView(CreateView):
    model = Dog
    fields = ("name", "breed", "photo")
    success_url = reverse_lazy("dogs:breeds")


class DogUpdateView(UpdateView):
    model = Dog
    fields = ("name", "breed", "photo", "birth_day")

    def get_success_url(self):
        return reverse("dogs:dogs_breeds", args=[self.object.breed.pk])


class DogDeleteView(DeleteView):
    model = Dog

    def get_success_url(self):
        return reverse("dogs:dogs_breeds", args=[self.object.breed.pk])
