from django.db import models

# Create your models here.
class telefonoModel(models.Model):
    name = models.Charfield(max_length = 100)
    brand = models.TextField(())
    sell_date = models.DateTimeField(auto_now = True)
    

def __str__(self):
    return self.name

class Meta:
    app_label = 'app1'