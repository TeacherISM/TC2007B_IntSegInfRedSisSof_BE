from django.db import models

# Create your models here.
class Nft(models.Model):
    title = models.CharField(max_length=255)
    metadata = models.CharField(max_length=255)
    price = models.BigIntegerField()

def __str__(self):
    return self.title

class Meta:
    app_label = 'app1'