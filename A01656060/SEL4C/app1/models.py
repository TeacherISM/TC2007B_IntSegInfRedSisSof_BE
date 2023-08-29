from django.db import models

# Create your models here.
class ActivityModel(models.Model):
    name = models.CharField(max_length=100)
    question=models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        app_label = 'app1'