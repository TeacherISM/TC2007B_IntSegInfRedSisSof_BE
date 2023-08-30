from django.db import models

# Create your models here.

class RecetaModel(models.Model):
    name = models.CharField(max_length=150)
    ingredients = models.TextField()
    procedure = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        app_label = 'app1'
