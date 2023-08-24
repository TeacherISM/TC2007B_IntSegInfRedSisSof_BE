from django.db import models

# Create your models here.
class TelefonoModel(models.Model):
    name = models.TextField()
    brand = models.CharField(max_length=50)
    quantity = models.BigIntegerField()
    

def __str__(self):
    return self.name

class Meta:
    app_label = 'app1'