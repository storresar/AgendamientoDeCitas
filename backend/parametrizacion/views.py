from rest_framework import viewsets
from .models import parametrizacion
from .serializers import parametrizacion_serializer

class Parametrizacion_Viewset(viewsets.ModelViewSet):
    queryset = parametrizacion.objects.all()
    serializer_class = parametrizacion_serializer


# Create your views here.
