from .models import Perros
from rest_framework import viewsets, permissions
from .serializers import PerrosSerializer

class PerrosViewSet(viewsets.ModelViewSet):
    queryset = Perros.objects.all() #Consulta todos los datos de la tabla
    permission_classes = [permissions.AllowAny] #Permisos para acceder a la API
    serializer_class = PerrosSerializer 