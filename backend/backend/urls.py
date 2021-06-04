from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth', include('rest_framework.urls')),
    path('api/', include('usuarios.urls')),
    path('api/', include('auditoria.urls')),
    path('api/', include('parametrizacion.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
