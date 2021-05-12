from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class tipo_usuario(models.Model):
    nombre_rol = models.TextField(max_length=50)

class usuario(AbstractUser):
    TIPO_ROL = (
        (1, 'Paciente'),
        (2, 'Funcionario'),
        (3, 'Administrador'),
    )

    rol = models.ForeignKey(tipo_usuario, on_delete=models.CASCADE)

