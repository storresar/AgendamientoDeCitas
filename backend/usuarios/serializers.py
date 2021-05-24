from rest_framework import serializers
from .models import usuario
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from datetime import date
from django.contrib.auth import get_user, password_validation, authenticate
from .utilities import get_token_for_user


class usuario_serializer(serializers.ModelSerializer):
    ultima_activacion = serializers.SerializerMethodField()
    class Meta:
        model = usuario
        fields = ('id','username','password','first_name', 'last_name', 'email','fecha_nacimiento','rol','ultima_activacion')

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
        else:
            raise serializers.ValidationError('Correo invalido')
        return nuevo

    def get_ultima_activacion(self, instance):
        return int((date.today() - instance.ultima_activacion).days)
    
class usuario_login_serializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales son invalidas')
        self.context['user'] = user
        return data
    
    def create(self, data):
        token = get_token_for_user(user=self.context['user'])
        return self.context['user'], token

