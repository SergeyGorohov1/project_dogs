from django.shortcuts import render
from dogs.models import Dog, Breed

def index(request):
    context = {
        "object_list": Breed.objects.all()
    }
    return render(request, "dogs/index.html", context)