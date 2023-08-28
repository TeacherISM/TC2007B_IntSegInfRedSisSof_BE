from django.db import models

class HomeModel(models.Model):
    arquitecto = models.CharField(max_length=40)

    def __str__(self):
        return self.arquitecto
    class Meta:
        app_label = 'app1'
