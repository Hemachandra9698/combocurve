from django.db import models
from jsonfield import JSONField
# Implement your models here


class Weather(models.Model):
    date = models.DateField(auto_now_add=True)
    latitude = models.DecimalField(decimal_places=4, max_digits=7, blank=True)
    longitude = models.DecimalField(decimal_places=4, max_digits=7, blank=True)
    city = models.CharField(default='', blank=True, max_length=25)
    state = models.CharField(default='', blank=True, max_length=25)
    temperatures = JSONField()
