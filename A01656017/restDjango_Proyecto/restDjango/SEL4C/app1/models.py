from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Admin(AbstractUser):
    """ 
    Administrator, inherits from AbstractUser.
    """
    username = models.CharField(max_length=40, unique=True)
    correo = models.CharField(max_length=40, unique=True)
    firstname = models.TextField()
    lastname = models.TextField()
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "correo"

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"
    class Meta:
        app_label = 'app1'

class Emprendedor(models.Model):
    """ 
    Emprendedor 
    """
    username = models.CharField(max_length=40, unique=True, primary_key=True)
    correo = models.CharField(max_length=40, unique=True)
    firstname = models.TextField()
    lastname = models.TextField()
    degree = models.TextField()
    institution = models.TextField()
    gender = models.TextField()
    age = models.IntegerField()
    country = models.TextField()
    studyField = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"
    class Meta:
        app_label = 'app1'


class Actividad(models.Model):
    idActividad = models.BigAutoField(default=0, primary_key=True)
    numAct = models.IntegerField()
    username = models.ForeignKey(Emprendedor, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.numAct} ({self.username})"
    class Meta:
        app_label = 'app1'


class Archivo(models.Model):
    idArchivo = models.BigAutoField(default=0, primary_key=True)
    idActividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    archivo = models.FileField()
    filetype = models.TextField()

    def __str__(self) -> str:
        return f"{self.numAct} ({self.idActividad})"
    class Meta:
        app_label = 'app1'


class Pregunta(models.Model):
    idPregunta = models.BigAutoField(default=0, primary_key=True)
    idActividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.idPregunta}. ({self.description})"
    class Meta:
        app_label = 'app1'


class Respuesta(models.Model):
    idRespuesta = models.BigAutoField(default=0, primary_key=True)
    idPregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    numero = models.IntegerField(default=0)
    texto = models.TextField(default="N/A")
    
    def __str__(self) -> str:
        return f"{self.idPregunta}.{self.idRespuesta}"
    class Meta:
        app_label = 'app1'

