from rest_framework import serializers
from .models import usuario,paciente
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from datetime import date, datetime
from django.contrib.auth import authenticate
from .utilities import get_token_for_user
from django.shortcuts import get_object_or_404
from parametrizacion.models import parametrizacion


class usuario_serializer(serializers.ModelSerializer):
    ultima_activacion = serializers.SerializerMethodField()

    class Meta:
        model = usuario
        fields = ('id','username','password','first_name', 'last_name', 'email','fecha_nacimiento','rol','ultima_activacion', 'activo', 'date_joined','intentos_loggeo',)
        read_only_fields = ('date_joined','intentos_loggeo',)

    def create(self, validated_data):
        mensaje = parametrizacion.objects.filter(nombre='correo', estado=True)
        try:
            mensaje = get_object_or_404(mensaje)
            mensaje = mensaje.valor
        except:
            mensaje = 'Felicidades! Usted se ha registrado exitosamente en Sofhy hostpital.\n'
            mensaje += 'A continuacion mostaremos sus credenciales, por favor no las difunda con nadie mas.'
        
        mensaje += '\nUsuario:  ' + validated_data['username'] + '\n'
        mensaje += 'Contraseña:  ' + validated_data['password'] + '\n'

        if send_mail(subject='Creacion de cuenta',message=mensaje,from_email=None,recipient_list=[validated_data['email']]) > 0:
            nuevo = usuario.objects.create(
                password = make_password(validated_data.pop('password')),
                **validated_data
            )
        else:
            raise serializers.ValidationError('Correo invalido')
        return nuevo

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username')
        if instance.password != validated_data.get('password'):
            instance.password = make_password(validated_data.get('password'))
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.email = validated_data.get('email')
        instance.fecha_nacimiento = validated_data.get('fecha_nacimiento')
        if  instance.activo == False and validated_data.get('activo') == True:
            instance.ultima_activacion = datetime.now().date()
        instance.activo = validated_data.get('activo')
        instance.rol = validated_data.get('rol')
        if instance.activo:
            instance.intentos_loggeo = 0
        instance.save()
        return instance
        
    def get_ultima_activacion(self, instance):
        return int((date.today() - instance.ultima_activacion).days)
    
class usuario_login_serializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            try:
                query = usuario.objects.filter(username=data['username'])
                usu = get_object_or_404(query)
                if not usu.check_password(data['password']):
                    usu.intentos_loggeo += 1
                    usu.save()
                    raise serializers.ValidationError('La contraseña es invalida')
            except:
                serializers.ValidationError('Usuario no encontrado')
            raise serializers.ValidationError('Las credenciales son invalidas')
        self.context['user'] = user
        return data
    
    def create(self, data):
        token = get_token_for_user(user=self.context['user'])
        return self.context['user'], token


class paciente_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = paciente
        fields = '__all__'
