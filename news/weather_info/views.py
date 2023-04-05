import os

import requests
from django.shortcuts import redirect
from djoser import permissions

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from notable_places.models import Place
from weather_info.models import Weather
from weather_info.serializers import WeatherSerializers


class WeatherViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = WeatherSerializers
    permission_classes = [permissions.permissions.IsAuthenticated]

    @action(methods=["post"], detail=True)
    def weather_create(self, request, pk, *args, **kwargs):
        if request.method == "POST":
            current_place = Place.objects.get(id=pk)
            appid = os.getenv('API_WEATHER_KEY')
            url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&units=metric&lon={}&appid=' + appid
            lon = current_place.lon
            lat = current_place.lat
            res = requests.get(url.format(lat, lon)).json()
            place_info = {
                'temperature': res["main"]["temp"],
                'pressure': res["main"]["pressure"],
                'windy_speed': res["wind"]["speed"],
                'place': pk
            }
            serializer = self.get_serializer(data=place_info)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
