from django.db import models
from django.conf import settings
# Create your models here.

class country_id(models.Model):
    id = models.BigAutoField(primary_key=True)
    Country = models.TextField()

    def __str__(self):
            return f'{self.id}, {self.Country}'


class Global_tem(models.Model):
    id = models.BigAutoField(primary_key=True)
    Country = models.ForeignKey()
    dt = models.TextField()
    AverageTemperature = models.TextField()
    AverageTemperatureUncertainty = models.TextField()
    City = models.TextField()
    Latitude = models.TextField()
    Longitude = models.TextField()

    def __str__(self):
            return f'{self.id}, {self.Country}, {self.dt},{self.AverageTemperature},{self.AverageTemperatureUncertainty},{self.City},{self.Latitude},{self.Longitude}'






