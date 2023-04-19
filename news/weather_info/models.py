from datetime import datetime

from django.db import models

from notable_places.models import Place


class Weather(models.Model):
    temperature = models.FloatField()
    pressure = models.FloatField()
    windy_speed = models.FloatField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date = models.DateField(default=datetime(2020, 1, 1))
