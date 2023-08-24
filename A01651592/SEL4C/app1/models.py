from django.db import models

#poner notación húngara
class AlumnoModel(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        app_label = 'app1'