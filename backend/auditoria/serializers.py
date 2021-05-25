from rest_framework import serializers
from .models import auditoria
# Create your models here.

class auditoria_serializer(serializers.ModelSerializer):
    class Meta():
        model = auditoria
        fields = "__all__"
