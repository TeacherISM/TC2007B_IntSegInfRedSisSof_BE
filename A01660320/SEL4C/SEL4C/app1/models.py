from django.db import models

# Create your models here.

class directorio (models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + " " + self.apellidos

class Meta:
    app_label = 'app1'