from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DetailView, TemplateView
from django.contrib.auth.views import LoginView

from app_pokemons.models import Pokemon
from .forms import RegistrationForm, LoginForm
from .models import User


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')


class RegistrationView(SuccessMessageMixin, CreateView):
    template_name = 'users/registration.html'
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    success_message = 'Registration successful'


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'


def favorite_pokemon(request, pokemon_id):
    user = User.objects.get(id=request.user.id)
    pokemon = Pokemon.objects.get(id=pokemon_id)
    user.pokemons.add(pokemon)

    return HttpResponseRedirect(reverse('pokemon_list'))
