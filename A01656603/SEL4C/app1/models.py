from django.db import models

# Create your models here.

class UsuarioModel(models.Model):
    user_email = models.CharField(max_length=100)
    user_fname = models.CharField(max_length=100)
    user_lname = models.CharField(max_length=100)
    user_level= models.CharField(max_length=100)
    user_school = models.CharField(max_length=100)
    user_gender = models.CharField(max_length=100)
    user_age = models.IntegerField() 
    user_country = models.CharField(max_length=100)
    user_schooln = models.CharField(max_length=100)
    user_notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User {self.user_email} | Name {self.user_fname} {self.user_lname}'