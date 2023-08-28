from django.db import models

# Create your models here.
class SatelliteModel(models.Model):
    # Attributes
    name = models.CharField(max_length=100)
    date_launched = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    # Methods
    def __str__(self):
        return self.name
    
    def getPosition(self):
        return (self.latitude, self.longitude)
    
    class Meta:
        app_label = 'app1'