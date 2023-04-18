import requests
from .models import Type, Stats, Pokemon


def create_pokemon():
    for i in range(1, 6):
        URL = f'https://pokeapi.co/api/v2/pokemon/{i}/'
        response = requests.get(url=URL).json()
        Pokemon.objects.create(name=response['name'])
        for type in response['types']:
            Type.objects.create(type_name=type['type']['name'], pokemon=Pokemon.objects.last())
        for stat in response['stats']:
            Stats.objects.create(stat_name=stat['stat']['name'], pokemon=Pokemon.objects.last())


create_pokemon()
