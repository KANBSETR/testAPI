from rest_framework import serializers
from .models import Perros


class PerrosSerializer(serializers.ModelSerializer): #Convertir el modelo
    class Meta:
        model = Perros
        fields = ('id', 'nombre', 'raza', 'edad', 'peso', 'fecha_ingreso',)
        read_only_fields = ('fecha_ingreso',) #No se puede modificar la fecha de ingreso(Evita que se modifique la fecha de ingreso)
    