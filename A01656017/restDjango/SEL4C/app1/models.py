from django.db import models

# Create your models here.
class Emprendedor(models.Model):
    nombre = models.TextField
    correo = models.EmailField

    def __str__(self) -> str:
        return self.nombre
    class Meta:
        app_label = 'app1'