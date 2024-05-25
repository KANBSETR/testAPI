from rest_framework import viewsets
from .serializers import PerrosSerializer, RefugioSerializer
from .models import Perros, Refugio
# Create your views here.

class PerrosViewSet(viewsets.ModelViewSet):
    queryset = Perros.objects.all()
    serializer_class = PerrosSerializer

class RefugioViewSet(viewsets.ModelViewSet):
    queryset = Refugio.objects.all()
    serializer_class = RefugioSerializer    