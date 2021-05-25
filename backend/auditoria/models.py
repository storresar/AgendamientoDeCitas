from django.db import models

class auditoria(models.Model):
    
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=20)
    usuario_cambio = models.CharField(max_length=20)
    usuario_realiza =  models.CharField(max_length=20)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.tipo