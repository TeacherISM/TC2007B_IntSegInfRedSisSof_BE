from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    genero = models.CharField(max_length=4)

def __str__(self):
    return self.nombre
class Meta:
    app_label = 'app1'
