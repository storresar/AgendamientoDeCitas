from rest_framework import routers, urlpatterns
from .views import usuario_viewset, mandar_correo, verificar_captcha, reactivar_usuario, paciente_view
from django.urls import path

router = routers.DefaultRouter()
router.register(r'usuarios', usuario_viewset)
router.register(r'pacientes',paciente_view)


urlpatterns = [
    path('mandar_correo/',mandar_correo),
    path('verificar_captcha/', verificar_captcha),
    path('reactivar_usuario/', reactivar_usuario)
]

urlpatterns += router.urls

