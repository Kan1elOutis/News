from rest_framework import serializers

from weather_info.models import Weather


class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'