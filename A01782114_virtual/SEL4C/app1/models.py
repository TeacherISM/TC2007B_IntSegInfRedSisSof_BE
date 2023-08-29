from django.db import models

# Create your models here.

class Schools(models.Model):
    name = models.CharField(max_length=100)
    numOfStudents = models.IntegerField()
    state = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        app_label = 'app1'