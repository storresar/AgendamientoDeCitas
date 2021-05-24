from rest_framework import routers, urlpatterns
from .views import usuario_viewset, mandar_correo
from django.urls import path

router = routers.DefaultRouter()
router.register(r'usuarios', usuario_viewset)


urlpatterns = [
    path('mandar_correo/',mandar_correo),
]

urlpatterns += router.urls

