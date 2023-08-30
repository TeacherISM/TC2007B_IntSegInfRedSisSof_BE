from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'Usuario {self.email} | Name {self.name}'

class Admin(models.Model):
    email = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return f'Administrator {self.email} | Name {self.name} | level of access {self.level}'
