from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.

class tipo_usuario(models.Model):
    nombre_rol = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre_rol

class usuario(AbstractUser):
    rol = models.ForeignKey(tipo_usuario, on_delete=models.CASCADE,null=True)
    fecha_nacimiento = models.DateField(null=True)
    
    def getEdad(self):
        return int((datetime.now().date() - self.fechaNacimiento).days / 365.25)
    
class tipo_identificacion(models.Model):
    nom_tipo_identificacion = models.TextField(max_length=25)

class paciente(models.Model):
    RH = models.TextField(max_length=3)
    sexo = models.CharField(max_length=1)
    usuario_p = models.OneToOneField(usuario, on_delete=models.CASCADE, null=False)
    tipo_identificacion = models.ForeignKey(tipo_identificacion, on_delete=models.DO_NOTHING)
    numero_identificacion = models.TextField(max_length=15)
