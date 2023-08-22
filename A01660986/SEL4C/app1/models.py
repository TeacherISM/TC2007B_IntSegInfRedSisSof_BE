from django.db import models

class Reminder(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.title
    class Meta:
        verbose_name = "Reminder"
        verbose_name_plural = "Reminders"

# Create your models here.
