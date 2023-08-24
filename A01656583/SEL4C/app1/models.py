from django.db import models

# Create your models here.
class ActivityModel(models.Model):
    activity_number = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Activity number: {self.activity_number} - Content:{self.title}"
    class Meta:
        app_label = 'app1'