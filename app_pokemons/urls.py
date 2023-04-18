from django.urls import path
from . import views
from .models import *

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemons/', views.pokemon_list, name='pokemon_list'),
]