from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
