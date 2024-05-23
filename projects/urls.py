from rest_framework import routers
from .api import PerrosViewSet

router = routers.DefaultRouter()
router.register('api/perros', PerrosViewSet, 'perros') #Registra la URL de la API

urlpatterns = router.urls #Muestra las URL de la API