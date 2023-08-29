from django.db import models

# Create your models here.

class  Token(models.Model):
    Tokens = models.CharField(max_length=10)
    activity = models.TextField()
    graded_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"Activity: {self.activity} Tokens: {self.Tokens} Graded at: {self.graded_at}"
    
    class Meta:
       app_label = 'app1'
