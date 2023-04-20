from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import RegistrationForm
from .models import User


class LoginView(TemplateView):
    template_name = 'users/login.html'


class RegistrationView(SuccessMessageMixin, CreateView):
    template_name = 'users/registration.html'
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    success_message = 'Registration successful'

