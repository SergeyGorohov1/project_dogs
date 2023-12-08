from django.db import models

NULLABLE = {"blank": True, "null": True}


class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Dogs(models.Model):
    name = models.CharField(max_length=100, verbose_name="Кличка")
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Порода")
    photo = models.ImageField(upload_to="dogs/", **NULLABLE, verbose_name="Фото")
    birth_day = models.DateField(**NULLABLE, verbose_name="Дата рождения")

    def __str__(self):
        return f"{self.name} {self.breed}"

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
