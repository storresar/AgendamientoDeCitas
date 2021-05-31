from django.db.models import query
from .utilities import get_token_for_user
from rest_framework import viewsets
from .serializers import usuario_serializer, usuario_login_serializer, paciente_serializer
from .models import usuario,paciente
from .permissions import IsUserOrAdmin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from django.core.mail import send_mail
from django.conf import settings
from auditoria.models import auditoria
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
        nueva_auditora = auditoria(
         tipo='Creación usuario',
         usuario_realiza= request.user,
         usuario_cambio=request.data['username'],
         ip=request.META.get('REMOTE_ADDR')
         )
        nueva_auditora.save()
        return super().create(request)

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = usuario_login_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user, token = serializer.save()
            if user.activo:
                usuario = usuario_serializer(user).data
                if usuario['ultima_activacion'] < 30:
                    data = {
                        'usuario': usuario,
                        'token': token
                    }
                    return Response(data, status=201)
                else:
                    #Bloqueo Usuario
                    user.activo = False
                    user.save()
                    return Response(data='Usuario Bloqueado', status=401)
            else:
                return Response(data='Usuario no activo', status=401)
        
    @action(detail=False, methods=['post'])
    def reactivar_usuario(self, request, pk=None):
        queryset = usuario.objects.filter(username=pk)
        user = get_object_or_404(queryset)
        if request.data['clave'] == request.data['confirma']:
            user.password = request.data['clave']
            user.save()
            return Response(data='Usuario actualizado exitosamente', status=200)
        else:
            return Response('Error en la peticion', status=400)

@api_view(['POST'])
def mandar_correo(request):
    usuario_bloqueado = usuario.objects.filter(email=request.data['email'])
    usu = get_object_or_404(usuario_bloqueado)
    nuevo_token = get_token_for_user(usu)
    mensaje = f'Querido usuario ' + usu.username
    mensaje += ' para desbloquear su cuenta acceda a este link a continuacion. Tienes 60 minutos. Que empiece el juego: \n'
    mensaje += f'127.0.0.1:8080/reactivar_usuario/?key={nuevo_token}?user={usu.username}'
    if (send_mail(subject='Desbloqueo',message=mensaje,from_email=None,recipient_list=[usu.email]) > 0):
        return Response('Correo enviado', status=200)

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

        user = usuario.objects.get(id=request.data.usuario_p)

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
        print('Siete')

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
