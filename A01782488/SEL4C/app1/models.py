from django.db import models

# Create your models here.

class UsrModel(models.Model):
    email = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Usuario: {self.email} | Nombre: {self.name} {self.lastName}'
