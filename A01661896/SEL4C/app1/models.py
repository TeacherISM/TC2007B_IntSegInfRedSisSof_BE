from django.db import models

# Create your models here.

class PCMaster(models.Model):
    procesador = models.CharField("Procesador",max_length=50)
    tarjetaGrafica = models.CharField("Grafica",max_length=50)
    NumVentiladores = models.IntegerField("Numero de ventiladores")
    FuentePoder = models.CharField("Fuente de poder",max_length=50)
    FechaConsulta = models.DateTimeField("Fecha de consulta",auto_now_add=True)

    def __str__(self):
        return self.tarjetaGrafica
    class Meta:
        app_label = 'app1'
    
    