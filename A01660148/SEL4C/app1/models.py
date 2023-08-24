from django.db import models

# Create your models here
class ticketGenerator(models.Model):
    id =  models.IntegerField()
    nombre = models.CharField(max_length=100)
    asiento = models.IntegerField()
    hora = models.ImageField()

    def __str__(self):
        return self.id
    
    class Meta:
        app_label = "boletos"
