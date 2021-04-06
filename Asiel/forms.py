from django import forms
from registration.forms import RegistrationFormUniqueEmail


class CorreoForm(forms.Form):
    Asunto = forms.CharField(max_length=100,min_length=10,required=True)
    Mensaje = forms.CharField(max_length=400,min_length=10,required=True)




class CustomForm(RegistrationFormUniqueEmail):
  pass