from rest_framework import viewsets
from .serializers import usuario_serializer
from .models import usuario
from .permissions import IsUserOrAdmin
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class usuario_viewset(viewsets.ModelViewSet):

    queryset = usuario.objects.all()
    serializer_class = usuario_serializer
    permission_classes = [IsUserOrAdmin]

    def retrieve(self, request, pk=None):
        queryset = usuario.objects.filter(username=pk)
        user = get_object_or_404(queryset)
        serializer = usuario_serializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = usuario.objects.filter(username=pk)
        user = get_object_or_404(queryset)
        serializer = usuario_serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        queryset = usuario.objects.filter(username=pk)
        user = get_object_or_404(queryset)
        user.delete()
        return self.list(request)
    
