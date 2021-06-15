from django.db import models

class parametrizacion(models.Model):
    nombre = models.CharField(max_length = 30)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    valor = models.CharField(max_length = 250)
    estado = models.BooleanField()
    