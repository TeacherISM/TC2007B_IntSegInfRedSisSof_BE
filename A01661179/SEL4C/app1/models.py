from django.db import models

class userApp(models.Model):
    email= models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    grade=models.CharField(max_length=100)
    institution=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    age=models.IntegerField()
    nation=models.CharField(max_length=100)
    study=models.CharField(max_length=100)

    def __str__(self):
        return f'Mail {self.email} - Name {self.name}'
    
    class Meta:
        app_label ='app1'
