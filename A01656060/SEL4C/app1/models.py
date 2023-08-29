from django.db import models

# Create your models here.
class ActivityModel(models.Model):
    name = models.CharField(max_length=100)
    question=models.TextField()
    done = models.BooleanField

    def __str__(self):
        return self.name
    class Meta:
        app_label = 'app1'

class AdvanceModel(models.Model):
    advanceNum = models.IntegerField

    def __str__(self):
        return self.advanceNum
    class Meta:
        app_label = 'app1'

class RetroModel(models.Model):
    retroFromAdmin = models.CharField(max_length=100)

    def __str__(self):
        return self.retroFromAdmin
    class Meta:
        app_label = 'app1'