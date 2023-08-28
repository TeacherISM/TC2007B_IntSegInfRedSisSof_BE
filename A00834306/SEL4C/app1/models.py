from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre=models.TextField()
    apellido=models.TextField()
    edad = models.BigIntegerField()

    def _str_(self):
        return self.title
    class Meta:
        app_label = "app1"