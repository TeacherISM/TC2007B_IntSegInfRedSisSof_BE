from django.db import models

class AguasFrescas(models.Model):
    nombre_agua = models.CharField(max_length=100)
    litros = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre_agua
    #class Meta:
#        app_label = 'app1'

class Clientes(models.Model):
    numero_de_cliente = models.IntegerField()
    
    def __str__(self):
        return f"Cliente {self.numero_de_cliente}"
    #class Meta:
     #   app_label = 'app1'

class Ventas(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    agua_fresca = models.ForeignKey(AguasFrescas, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Venta {self.id} - Cliente {self.cliente.numero_de_cliente} - Agua {self.agua_fresca.nombre_agua}"
    #class Meta:
     #   app_label = 'app1'
