from rest_framework import serializers
from .models import usuario
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail


class usuario_serializer(serializers.ModelSerializer):

    class Meta:
        model = usuario
        fields = ('id','username','password','first_name', 'last_name', 'email','fecha_nacimiento','rol')

    def create(self, validated_data):
        mensaje = 'Felicidades! Usted se ha registrado exitosamente en Sophy hostpital.\n'
        mensaje += 'A continuacion mostaremos sus credenciales, por favor no las difunda con nadie mas.\n'
        mensaje += 'Usuario:  ' + validated_data['username'] + '\n'
        mensaje += 'Contraseña:  ' + validated_data['password'] + '\n'

        if send_mail(subject='Creacion de cuenta',message=mensaje,from_email=None,recipient_list=[validated_data['email']]) > 0:
            nuevo = usuario.objects.create(
                password = make_password(validated_data.pop('password')),
                **validated_data
            )
        return nuevo
    