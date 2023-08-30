from django.db import models

# Create your models here.
class Personalized(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.name
    
    class Meta:
        app_label = 'app1'