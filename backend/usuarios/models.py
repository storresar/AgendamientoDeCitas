from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from simple_history.models import HistoricalRecords

# Create your models here.

class tipo_usuario(models.Model):
    nombre_rol = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre_rol

class usuario(AbstractUser):
    email = models.EmailField(unique=True)
    rol = models.ForeignKey(tipo_usuario, on_delete=models.CASCADE, null=True)
    fecha_nacimiento = models.DateField(null=True)
    ultima_activacion = models.DateField(default=datetime.date.today)
    activo = models.BooleanField(default=True)
    history = HistoricalRecords()

    @property
    def edad(self):
        return int((datetime.date.today - self.fecha_nacimiento).days / 365.25)

    def __str__(self):
        return self.username
        
    
class tipo_identificacion(models.Model):
    nom_tipo_identificacion = models.TextField(max_length=25)

    def __str__(self):
        return self.nom_tipo_identificacion

class paciente(models.Model):
    RH = models.TextField(max_length=3)
    sexo = models.CharField(max_length=1)
    usuario_p = models.OneToOneField(usuario, on_delete=models.CASCADE, null=False)
    tipo_identificacion = models.ForeignKey(tipo_identificacion, on_delete=models.DO_NOTHING)
    numero_identificacion = models.TextField(max_length=15)
