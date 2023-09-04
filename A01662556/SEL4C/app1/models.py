from django.db import models

# Create your models here.

class Actividad(models.Model):
    titulo = models.CharField(default="",max_length=50)
    descripcion = models.CharField(default="", max_length=350)
    tokens = models.IntegerField(default=-1)

    def __str__ (self):
        return "{} - Tokens: {}".format(self.titulo, self.tokens)
