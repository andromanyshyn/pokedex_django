from django.db import models
from django.urls import reverse


class Pokemon(models.Model):
    name = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse('add_pokemon', kwargs={'pokemon_id': self.id})

    def __str__(self):
        return self.name


class Type(models.Model):
    type_name = models.CharField(max_length=32)
    pokemon = models.ForeignKey(to=Pokemon, on_delete=models.CASCADE)

    class Meta:
        ordering = ('type_name',)

    def __str__(self):
        return self.type_name


class Stats(models.Model):
    stat_name = models.CharField(max_length=32)
    pokemon = models.ForeignKey(to=Pokemon, on_delete=models.CASCADE)

    class Meta:
        ordering = ('stat_name',)

    def __str__(self):
        return self.stat_name
