from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings
from .models import *
from django.contrib.auth.views import PasswordChangeForm
from django.contrib.auth.forms import SetPasswordForm

class LoginForm (AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'input100'
            i.field.widget.attrs['placeholder'] = i.name
            i.field.widget.attrs['autocomplete'] = 'off' 



class FormRegistro(UserCreationForm):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'


    first_name=forms.CharField(
        max_length=30,
        min_length=2,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre'})
        )
        
    last_name=forms.CharField(
        max_length=30,
        min_length=2,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Apellido'})
        )

 


    class Meta:
        model=User
                
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            
        )
        widgets={
           
        
            'username': forms.TextInput(attrs={
                'placeholder':'Usuario',
                'autocomplete':'off'}),
            
            'email': forms.EmailInput(attrs={
                'placeholder':'Correo Electronico',
                'autocomplete':'off',
                'required':'true'
                }),         

            
            

        }

        error_messages={
        
            'username':{
                'unique': "Ya existe una cuenta con este nombre de usuario",
                'required': "Tiene que escribir un usuario",
                'max_length': "Usuario demasiado largo",
                'min_length': "Usuario demasiado corto",  
                },

            'email':{

                'required': "Debe escribir un correo",
                'invalid': "Direccion de correo no valida",  
                },

           
        }
       
