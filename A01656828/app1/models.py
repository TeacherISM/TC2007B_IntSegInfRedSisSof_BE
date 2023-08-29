from django.db import models

# Create your models here.
class CustomModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' + self.last_name
    
    class Meta:
        verbose_name = 'Custom Model'
        verbose_name_plural = 'Custom Models'
        ordering = ['name']
        app_label = 'app1'