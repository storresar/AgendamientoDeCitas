from rest_framework import routers, urlpatterns
from rest_framework import viewsets
from .views import AuditoriaViewSet

router = routers.DefaultRouter()

router.register(r'auditoria', AuditoriaViewSet,basename='auditoria')

urlpatterns = router.urls