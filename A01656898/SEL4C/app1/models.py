from django.db import models
from datetime import timedelta
import datetime

# Create your models here.
class HomeUser(models.Model):
    # Login Information
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    
    # User Information
    full_name = models.CharField(max_length = 255)  # divide in name(s) and other?
    email = models.EmailField(null = True)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    last_login = models.DateTimeField(null = True)
    time_spended = models.DurationField(default = timedelta(days = 0, hours = 0, minutes = 0, seconds = 0))
    rol = models.CharField(max_length = 15, choices = (("Usuario", "Usuario"), 
                                                       ("Administrador", "Administrador")), default = "Usuario")

    # Data analysis    
    birth = models.DateField(null = True)
    genre = models.CharField(max_length = 255, null = True)
    country = models.CharField(max_length = 255, null = True)       # Text box or combo box?
    institution = models.CharField(max_length = 255, null = True)
    carrer = models.CharField(max_length = 30, choices = (("Ingeniería y Ciencias", "Ingeniería y Ciencias"), 
                                                          ("Humanidades y Educación", "Humanidades y Educación"),
                                                          ("Ciencias Sociales", "Ciencias Sociales"), 
                                                          ("Ciencias de la Salud", "Ciencias de la Salud"),
                                                          ("Arquitectura, Arte y Diseño", "Arquitectura, Arte y Diseño"),
                                                          ("Negocios", "Negocios")), null = True)

    grade = models.CharField(max_length = 20, choices = (("Pregrado", "Pregrado"), 
                                                         ("Posgrado", "Posgrado"), 
                                                         ("Educación continua", "Educación continua")), null = True)
    
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        app_label = "app1"

