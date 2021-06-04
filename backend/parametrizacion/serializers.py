from django.db.models import fields
from django.db.models.base import Model
from django.db.models.fields import files
from  .models import parametrizacion
from rest_framework import serializers

class parametrizacion_serializer(serializers.ModelSerializer):
    class Meta():
        model = parametrizacion
        fields = "__all__"


