from rest_framework import viewsets
from .models import parametrizacion
from .serializers import parametrizacion_serializer
from django.utils import timezone
from auditoria.models import auditoria

class Parametrizacion_Viewset(viewsets.ModelViewSet):
    queryset = parametrizacion.objects.all()
    serializer_class = parametrizacion_serializer

    def list(self, request, *args, **kwargs):
        queryset = parametrizacion.objects.all()
        for i in queryset:
            if i.fecha_fin < timezone.now().date():
                i.estado = False
            elif i.fecha_inicio > timezone.now().date():
                i.estado = False
            else:
                i.estado = True
            i.save()
                
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        nueva_auditora = auditoria(
            tipo='Creación parametro',
            usuario_realiza= request.user,
            usuario_cambio=request.data['nombre'],
            ip=request.META.get('REMOTE_ADDR')
            )
        nueva_auditora.save()
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        nueva_auditora = auditoria(
            tipo='Modificación parametro',
            usuario_realiza= request.user,
            usuario_cambio=request.data['nombre'],
            ip=request.META.get('REMOTE_ADDR')
            )
        nueva_auditora.save()
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        nueva_auditora = auditoria(
            tipo='Eliminación parametro',
            usuario_realiza= request.user,
            usuario_cambio=request.data['nombre'],
            ip=request.META.get('REMOTE_ADDR')
            )
        nueva_auditora.save()
        return super().destroy(request, *args, **kwargs)


# Create your views here.
