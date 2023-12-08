from django.db import models

NULLABLE = {"blank": True, "null": True}

class Dogs(models.Model):
    name = models.CharField(max_length=100, verbose_name="Кличка")
    breed = models.CharField(max_length=100, verbose_name="Порода")
    photo = models.ImageField(upload_to="dogs/", **NULLABLE, verbose_name="Фото")
    birth_day = models.DateField(**NULLABLE, verbose_name="Дата рождения")


    def __str__(self):
        return f"{self.name} {self.breed}"

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"