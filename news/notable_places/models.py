from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_admin_geomap import GeoItem


class Place(models.Model, GeoItem):
    @property
    def geomap_longitude(self):
        return str(self.lon)

    @property
    def geomap_latitude(self):
        return str(self.lat)

    @property
    def geomap_popup_view(self):
        return "<strong>{}</strong>".format(str(self))

    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view

    name = models.CharField(max_length=256)
    lon = models.FloatField(default=0)  # долгота
    lat = models.FloatField(default=0)  # широта
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)])

    def __str__(self):
        return f'{self.name}'
