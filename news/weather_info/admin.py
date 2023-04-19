from django.contrib import admin
from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export.resources import ModelResource

from weather_info.models import Weather


class WeatherResource(ModelResource):
    class Meta:
        model = Weather


@admin.register(Weather)
class WeatherAdmin(ImportExportActionModelAdmin, ModelAdmin):
    resource_class = WeatherResource
    list_display = ('temperature', 'pressure', 'windy_speed', 'place', 'date')
    fields = ('place', 'temperature', 'pressure', 'windy_speed', 'date')
    readonly_fields = ['temperature', 'pressure', 'windy_speed', 'place', 'date']
    list_filter = ['place', 'date']
