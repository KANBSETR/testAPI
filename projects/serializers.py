from rest_framework import serializers
from .models import Perros, Refugio


class PerrosSerializer(serializers.ModelSerializer): #Convertir el model
    class Meta:
        model = Perros
        fields = ('id', 'nombre', 'raza', 'edad', 'peso', 'fecha_ingreso',)
        read_only_fields = ('fecha_ingreso',) #No se puede modificar la fecha de ingreso(Evita que se modifique la fecha de ingreso)
    
    
class RefugioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refugio
        # fields = ('id', 'nombre', 'direccion', 'telefono', 'email', 'perros', 'is_active',)
        fields = '__all__'
        
        
