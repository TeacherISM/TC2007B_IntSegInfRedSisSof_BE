from django.db import models

# Create your models here.

class BookModel(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=130)
    summary = models.TextField()

    def __str__(self):
        return self.author 
    
    ##class Meta: 
    ##    app_label = 'app1'

