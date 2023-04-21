from django.contrib.auth.models import AbstractUser
from django.db import models

from django.urls import reverse

from app_pokemons.models import Pokemon


class User(AbstractUser):
    pokemons = models.ManyToManyField(to=Pokemon)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.id})
