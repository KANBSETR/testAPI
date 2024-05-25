from rest_framework import routers
#from .api import PerrosViewSet

from django.urls import path, include
from projects import views
from .views import PerrosViewSet, RefugioViewSet

"""
router = routers.DefaultRouter()
router.register('api/perros', PerrosViewSet, 'perros') #Registra la URL de la API

urlpatterns = router.urls #Muestra las URL de la API
"""


routerPerros = routers.DefaultRouter()
routerPerros.register(r'perros',views.PerrosViewSet) #Registra la URL de la API


routerRefugio = routers.DefaultRouter()
routerRefugio.register(r'refugio',views.RefugioViewSet) #Registra la URL de la API


urlpatterns = [
    path('api1/', include(routerPerros.urls)),
    path('api2/', include(routerRefugio.urls)),
]
