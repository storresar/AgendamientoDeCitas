from rest_framework import viewsets
from .serializers import usuario_serializer
from .models import usuario
from .permissions import IsUserOrAdmin

class usuario_viewset(viewsets.ModelViewSet):

    queryset = usuario.objects.all()
    serializer_class = usuario_serializer
    permission_classes = [IsUserOrAdmin]

    
