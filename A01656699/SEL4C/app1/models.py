from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    contraseña = models.TextField()
    edad = models.IntegerField()
    genero = models.TextField()
    puntuacion = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        app_label = 'app1'
