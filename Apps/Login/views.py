from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.contrib.auth.views  import LoginView
from .forms import *
# Create your views here.

class IniciarSesionView(LoginView):
    template_name='Login/login.html'
    form_class = LoginForm


class RegisterView(FormView):
    template_name = "Login/register.html"
    form_class = FormRegistro
    success_url='/'
    
    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

   

 


