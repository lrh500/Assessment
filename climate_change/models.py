from django.db import models
from django.conf import settings
# Create your models here.

class country_id(models.Model):
    id = models.IntegerField()
    country = models.TextField(primary_key=True)

    def __str__(self):
            return f'{self.id}, {self.Country}'


class Global_tem(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.ForeignKey('climate_change.country_id',on_delete=models.CASCADE, related_name='global_tem')
    dt = models.TextField()
    averageTemperature = models.TextField()
    averageTemperatureUncertainty = models.TextField()
    city = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()

    def __str__(self):
            return f'{self.id}, {self.country}, {self.dt},{self.averageTemperature},{self.averageTemperatureUncertainty},{self.city},{self.latitude},{self.longitude}'





