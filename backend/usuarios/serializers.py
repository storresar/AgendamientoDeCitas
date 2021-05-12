from django.db.models import fields, query_utils
from rest_framework import serializers
from .models import usuario, tipo_usuario



class usuario_serializer(serializers.ModelSerializer):

    class Meta:
        model = usuario
        fields = ('username','password','first_name', 'last_name', 'email','fecha_nacimiento','rol')

