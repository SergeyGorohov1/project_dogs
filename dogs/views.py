from django.shortcuts import render
from dogs.models import Dog, Breed

def index(request):
    context = {
        "object_list": Breed.objects.all()[:3]
    }
    return render(request, "dogs/index.html", context)


def breeds(request):
    context = {
        "object_list": Breed.objects.all()
    }
    return render(request, "dogs/index.html", context)