from django.contrib import admin

from dogs.models import Dog, Breed


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ("name", "breed")
    list_filter = ("name", "breed", "birth_day")
    search_fields = ("name", "breed")



@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass
