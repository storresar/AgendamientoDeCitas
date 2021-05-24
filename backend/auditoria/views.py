from rest_framework import viewsets
from .serializers import log_history_serializer
from .permissions import ReadOnly 
from django.contrib.admin.models import LogEntry

# ADDITION = 1
# CHANGE = 2
# DELETION = 3

class log_viewset(viewsets.ModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = log_history_serializer
    permission_classes = [ReadOnly]



