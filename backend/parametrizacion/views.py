from rest_framework import viewsets
from .models import parametrizacion
from .serializers import parametrizacion_serializer
from django.utils import timezone

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


# Create your views here.
