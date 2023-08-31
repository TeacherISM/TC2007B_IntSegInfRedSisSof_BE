from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    en_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        app_label = 'appl'
