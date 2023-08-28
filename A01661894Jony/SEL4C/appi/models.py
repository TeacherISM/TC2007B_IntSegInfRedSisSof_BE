from django.db import models

# Create your models here.

class CarSale(models.Model):
    brand = models.CharField("Marca del carro: ",max_length=50)
    specifications = models.TextField("Especificaciones")
    created_at = models.DateField("Fecha de consulta: ",auto_now_add=True)

    def __str__(self):
        return self.brand
    
    class Meta:
        app_label = 'appi'