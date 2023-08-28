from django.db import models

# Create your models here.
class StudentModel(models.Model):
    first_name = models.CharField("Nombre", max_length=100)
    last_name = models.CharField("Apellido", max_length=100)
    gender = models.CharField("Género", max_length=50)
    age = models.IntegerField("Edad")
    edu_lvl = models.CharField("Máximo nivel educativo", max_length=100)

    def __str__(self):
        return f"Name: {self.first_name} Last name: {self.last_name} Gender: {self.gender} Age: {self.age} Educational Level: {self.edu_lvl}" 
    class Meta:
        app_label = 'app1'