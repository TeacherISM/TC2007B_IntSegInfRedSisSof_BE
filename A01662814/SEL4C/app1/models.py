from django.db import models

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta1:
        app_label='app1'