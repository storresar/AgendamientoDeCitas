from rest_framework import viewsets
from .models import auditoria
from .serializers import auditoria_serializer


class AuditoriaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = auditoria.objects.all()
    serializer_class = auditoria_serializer