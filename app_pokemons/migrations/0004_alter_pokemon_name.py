# Generated by Django 4.2 on 2023-04-17 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pokemons', '0003_remove_pokemon_stats_remove_pokemon_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]