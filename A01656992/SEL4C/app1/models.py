from django.db import models

# Create your models here.
class Carro(models.Model):
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    color = models.CharField(max_length = 50)
    anio = models.PositiveIntegerField()

    def __str___(self):
        return self.marca

    class Meta:
        app_label = 'app1'