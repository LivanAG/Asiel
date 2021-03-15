from django.urls import include, path
from .views import *
from django.contrib.auth.views import LogoutView
app_name= 'Login'

urlpatterns = [
    path('Login',IniciarSesionView.as_view(),name='login'),
    path('CerrarSesion/',LogoutView.as_view(), name="logout"),
    path('Registro/',RegisterView.as_view(), name="register"),
]