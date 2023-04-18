from django.contrib import admin
from .models import Pokemon, Type, Stats


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'pokemon')


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ('stat_name', 'pokemon')