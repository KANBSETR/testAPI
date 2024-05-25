from django.db import models

class Perros(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    peso = models.FloatField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Refugio(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()
    perros = models.ManyToManyField(Perros)
    # is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
