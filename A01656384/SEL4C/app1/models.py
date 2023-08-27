from django.db import models

# Create your models here.
class Videogames(models.Model):
    name = models.CharField(max_length=50)
    character = models.CharField(max_length=50)
    level = models.BigIntegerField()

def __str__(self):
    return self.name
class Meta:
    app_label = 'app1'
