from django.contrib import admin
from django_admin_geomap import ModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export.resources import ModelResource

from notable_places.models import Place


class PlaceResource(ModelResource):
    class Meta:
        model = Place


@admin.register(Place)
class PlacesAdmin(ImportExportActionModelAdmin, ModelAdmin):
    resource_class = PlaceResource
    list_display = ('id', 'name', 'lon', 'lat', 'rating')
    fields = ('name', 'lon', 'lat', 'rating')
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"
