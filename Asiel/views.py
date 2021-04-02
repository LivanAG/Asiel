from django.conf import settings
from django.shortcuts import render
from .models import *
from .forms import *
from .urls import *
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView,FormView
from django.views.decorators.csrf  import csrf_exempt
from django.http import JsonResponse
from django.urls  import reverse_lazy
import smtplib
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from email.mime.multipart import MIMEMultipart
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

def enviar_mail(user,asunto,mensaje):
            # Establecemos conexion con el servidor smtp de gmail
            mailServer = smtplib.SMTP(settings.EMAIL_HOST,settings.EMAIL_PORT)
            print(mailServer.ehlo())# Comprueba si tenemos conexion y nos da la respuesta 
            mailServer.starttls() # Establece una conexion segura
            print(mailServer.ehlo())# Comprueba si tenemos conexion y nos da la respuesta 
            mailServer.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)

            email_to=settings.EMAIL_HOST_USER
            
            # Construimos el mensaje 
            mensaje = MIMEText(mensaje)
            mensaje['From']=user.email
            mensaje['To']=email_to
            mensaje['Subject']=asunto
        
            # Envio del mensaje
            mailServer.sendmail(user.email,email_to,mensaje.as_string())

        


class EnviarEmail(TemplateView):
    template_name = '/' 

    def post(self, request,*args,**kwargs):
        data={}

     
        try:
            id = request.POST['id']
            nombre = request.POST['name']
            email = request.POST['email']
            asunto = request.POST['subject']
            mensaje = request.POST['message']

            usuario_remitente = User.objects.get(id=id)
            if asunto:
                
                if mensaje:
                    Mensaje = mensaje + "\n\nEste correo fue enviado por el usuario\nNombre: " + usuario_remitente.first_name +"\nApellido: "+ usuario_remitente.last_name+"\nUsuario: "+ usuario_remitente.username+"\nid: " + str(usuario_remitente.id)+ "\nEmail: " +usuario_remitente.email
                    try:
                        enviar_mail(usuario_remitente,asunto,Mensaje)
                    except Exception as e:
                        data['error']='No se ha podido enviar el correo, Revise su conexion y vuelva a intentarlo'
                
                else:
                    data['error']='Debes Escribir un Mensaje'
            else:
                data['error']='Debes Escribir un Asunto'



        except Exception as e:
            data['error']=str(e)
        
        return JsonResponse(data)

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        return context


