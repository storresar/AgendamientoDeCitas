from rest_framework import routers
from .views import Parametrizacion_Viewset

router = routers.DefaultRouter()
router.register(r'parametrizacion',Parametrizacion_Viewset,basename='parametrizacion')
urlpatterns = router.urls

