from rest_framework import routers, urlpatterns
from .views import usuario_viewset, mandar_correo, verificar_captcha,paciente_view
from django.urls import path

router = routers.DefaultRouter()
router.register(r'usuarios', usuario_viewset)
router.register(r'pacientes',paciente_view)


urlpatterns = [
    path('mandar_correo/',mandar_correo),
    path('verificar_captcha/', verificar_captcha),
]

urlpatterns += router.urls

