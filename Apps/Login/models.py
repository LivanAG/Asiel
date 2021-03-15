from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

'''
class User(User):
    token = models.UUIDField(primary_key=False,editable=False,blank=True,null=True)   
    subscrito = models.BooleanField(default=False)
'''    