from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('add-pokemon/<int:pokemon_id>/', views.favorite_pokemon, name='add_pokemon'),
]
