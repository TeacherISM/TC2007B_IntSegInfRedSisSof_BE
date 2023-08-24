from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name + self.surname

    class Meta:
        app_label = "app1"


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        app_label = "app1"
