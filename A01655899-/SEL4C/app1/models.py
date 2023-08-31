from django.db import models


class BookModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13)
    
    def __str__(self):
        return self.title

    class Meta:
        app_label = 'app1'