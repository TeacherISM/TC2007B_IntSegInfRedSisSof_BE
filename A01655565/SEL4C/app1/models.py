from django.db import models

# Create your models here.
class Usuarios (models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.TextField()
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        app_label = 'app1'