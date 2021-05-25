from rest_framework import routers, urlpatterns
from .views import log_viewset

router = routers.DefaultRouter()

router.register(r'auditoria', log_viewset)

urlpatterns = router.urls