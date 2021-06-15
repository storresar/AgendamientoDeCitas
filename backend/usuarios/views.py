from datetime import datetime
from django.db.models import query
from rest_framework import response
from .utilities import get_token_for_user
from rest_framework import viewsets
from .serializers import usuario_serializer, usuario_login_serializer, paciente_serializer
from .models import usuario,paciente
from .permissions import IsUserOrAdmin
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from django.core.mail import send_mail
from django.conf import settings
from auditoria.models import auditoria
from parametrizacion.models import parametrizacion
from django.contrib.auth.hashers import make_password
import requests

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
        nueva_auditora = auditoria(
         tipo='Actualización usuario',
         usuario_realiza= request.user,
         usuario_cambio=pk,
         ip=request.META.get('REMOTE_ADDR')
         )
        nueva_auditora.save()
        queryset = usuario.objects.filter(username=pk)
        user = get_object_or_404(queryset)
        serializer = usuario_serializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        nueva_auditora = auditoria(
         tipo='Eliminación usuario',
         usuario_realiza= request.user,
         usuario_cambio=pk,
         ip=request.META.get('REMOTE_ADDR')
         )
        nueva_auditora.save()
        queryset = usuario.objects.filter(username=pk)
        user = get_object_or_404(queryset)
        user.delete()
        return self.list(request)

    def create(self, request):
        c_admins_permitidos = parametrizacion.objects.filter(nombre='admin', estado=True)
        try:
            c_admins_permitidos = get_object_or_404(c_admins_permitidos)
            c_admins_permitidos = int(c_admins_permitidos.valor)
        except:
            c_admins_permitidos = 6
        c_admins_actuales = usuario.objects.filter(rol=3).count()
        if request.data['rol'] == 3:
            c_admins_actuales += 1
            if c_admins_permitidos >= c_admins_actuales:

                nueva_auditora = auditoria(
                tipo='Creación usuario',
                usuario_realiza= request.user,
                usuario_cambio=request.data['username'],
                ip=request.META.get('REMOTE_ADDR')
                )
                nueva_auditora.save()

                return super().create(request)
            else:
                return Response('Limite superado para la creación de administradores', status=405)
        else:
            nueva_auditora = auditoria(
                tipo='Creación usuario',
                usuario_realiza= request.user,
                usuario_cambio=request.data['username'],
                ip=request.META.get('REMOTE_ADDR')
                )
            nueva_auditora.save()

            return super().create(request)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        c_dias_permitidos = parametrizacion.objects.filter(nombre='inactivar', estado=True)
        try:
            c_dias_permitidos = get_object_or_404(c_dias_permitidos)
            c_dias_permitidos = int(c_dias_permitidos.valor)
        except:
            c_dias_permitidos = 30
            
        serializer = usuario_login_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            user, token = serializer.save()
            print('Usuario', user.activo)
            if user.activo:
                usuario = usuario_serializer(user).data
                if usuario['ultima_activacion'] < c_dias_permitidos and usuario['intentos_loggeo'] < 3:
                    data = {
                        'usuario': usuario,
                        'token': token
                    }
                    return Response(data, status=201)
                else:
                    #Bloqueo Usuario
                    nueva_auditora = auditoria(
                    tipo='Usuario bloqueado',
                    usuario_realiza= 'Automatico',
                    usuario_cambio=usuario['username'],
                    ip=request.META.get('REMOTE_ADDR')
                    )
                    nueva_auditora.save()
                    user.activo = False
                    user.save()
                    return Response(data='Usuario Bloqueado', status=401)
            else:
                return Response(data='Usuario Bloqueado', status=401)
        else:
            return Response(data='Fallo en las credenciales', status=401)
        
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def reactivar_usuario(request):
    queryset = usuario.objects.filter(username=request.data['username'])
    user = get_object_or_404(queryset)
    print(user)
    if request.data['clave'] == request.data['confirma']:
        nueva_auditora = auditoria(
        tipo='Usuario desbloquedo',
        usuario_realiza= 'Automatico',
        usuario_cambio= user.username,
        ip=request.META.get('REMOTE_ADDR')
        )
        nueva_auditora.save()
        user.password = make_password(request.data['clave'])
        user.activo = True
        user.intentos_loggeo = 0
        user.ultima_activacion = datetime.now()
        user.save()
        return Response(data='Usuario actualizado exitosamente', status=200)
    else:
        return Response('Error en la peticion', status=400)

@api_view(['POST'])
@permission_classes((AllowAny,))
def mandar_correo(request):
    usuario_bloqueado = usuario.objects.filter(email=request.data['email'])
    try:
        usu = get_object_or_404(usuario_bloqueado)
        if usu.activo == False:
            nuevo_token = get_token_for_user(usu)
            mensaje = f'Querido usuario {usu.username}'
            mensaje += ' para desbloquear su cuenta acceda a este link a continuacion. Tienes 60 minutos. Que empiece el juego: \n'
            mensaje += f'https://sophyhospital.vercel.app/#/cambiar_clave/{nuevo_token}/{usu.username}'
            if send_mail(subject='Desbloqueo',message=mensaje,from_email=None,recipient_list=[usu.email]) > 0:
                return Response('Correo enviado', status=200)
        else:
            return Response('Este usuario esta activo', status=404)
    except:
        return Response('El usuario asociado a este correo no esta registrado', status=404)

@api_view(['POST'])
@permission_classes((AllowAny,))
def verificar_captcha(request):
    recaptcha_response = request.data['g-recaptcha-response']
    data = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result = r.json()
    if result['success']:
        return Response(True, status=r.status_code)
    else:
        return Response(False, status=r.status_code)

class paciente_view(viewsets.ModelViewSet):

    queryset = paciente.objects.all()
    serializer_class = paciente_serializer


    def retrieve(self, request, pk=None):

        queryset = paciente.objects.filter(usuario_p=pk)
        user = get_object_or_404(queryset)
        serializer = paciente_serializer(user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = usuario.objects.get(id=request.data.get('usuario_p'))

        nueva_auditora = auditoria(
         tipo='Creación paciente',
         usuario_realiza= request.user,
         usuario_cambio= user.username,
         ip=request.META.get('REMOTE_ADDR')
         )
        nueva_auditora.save()
        return super().create(request, *args, **kwargs)

    def update(self, request, pk=None):

        user = usuario.objects.get(id=pk)

        nueva_auditora = auditoria(
         tipo='Actualización Paciente',
         usuario_realiza= request.user,
         usuario_cambio= user.username,
         ip=request.META.get('REMOTE_ADDR')
         )
        nueva_auditora.save()

        queryset = paciente.objects.filter(usuario_p=pk)
        user = get_object_or_404(queryset)
        serializer = paciente_serializer(user, data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):

        user = usuario.objects.get(id=pk)

        nueva_auditora = auditoria(
         tipo='Eliminación Paciente',
         usuario_realiza= request.user,
         usuario_cambio= user.username,
         ip=request.META.get('REMOTE_ADDR')
         )
        nueva_auditora.save()
        queryset = paciente.objects.filter(usuario_p=pk)
        user = get_object_or_404(queryset)
        serializer = paciente_serializer(user, data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.delete()
            return Response('Eliminado')
        return Response(serializer.errors)
