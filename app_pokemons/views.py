from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView
from .models import Pokemon, Type, Stats


# from .create_pokemon import create_pokemon # !! Uncomment it, only if you want to create new Pokemons


def index(request):
    return render(request, 'app_pokemons/index.html')


def pokemon_list(request):
    if 'search_name' in request.GET:
        pokemons = Pokemon.objects.filter(name=request.GET['search_name'])
    else:
        pokemons = Pokemon.objects.all()
    if 'paginate' in request.GET:
        paginator = Paginator(pokemons, int(request.GET['paginate']))
    else:
        paginator = Paginator(pokemons, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'app_pokemons/pokemons.html', context={'page_obj': page_obj})
