from django.shortcuts import render
from django.views.generic import ListView

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
