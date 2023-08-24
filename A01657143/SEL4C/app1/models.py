from django.db import models

# Create your models here.
class catCreate(models.Model):
    nombre= models.CharField(max_length= 100)
    raza= models.CharField(max_length= 100)
    biografia= models.TextField()
    nacimiento=  models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre
    class Meta: 
        app_label = 'Bingus'