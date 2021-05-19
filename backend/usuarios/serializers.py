from django.db.models import fields, query_utils
from rest_framework import serializers
from .models import usuario, tipo_usuario
from django.contrib.auth.hashers import make_password


class usuario_serializer(serializers.ModelSerializer):

    class Meta:
        model = usuario
        fields = ('id','username','password','first_name', 'last_name', 'email','fecha_nacimiento','rol')

    def create(self, validated_data):
        nuevo = usuario.objects.create(
            password = make_password(validated_data.pop('password')),
            **validated_data
        )
        return nuevo
    