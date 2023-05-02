from django.db import models
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country,
        related_name="city",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
