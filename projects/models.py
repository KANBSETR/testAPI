from django.db import models

class Perros(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    peso = models.FloatField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
