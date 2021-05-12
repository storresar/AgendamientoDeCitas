from rest_framework import routers, urlpatterns
from .views import usuario_viewset

router = routers.DefaultRouter()
router.register(r'usuarios', usuario_viewset)

urlpatterns = router.urls