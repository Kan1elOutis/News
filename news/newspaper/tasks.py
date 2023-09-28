import os
from datetime import datetime

import requests
from django.core.mail import send_mail
from djoser.conf import User
from dotenv import load_dotenv

from news.celery import app
from notable_places.models import Place
from weather_info.models import Weather

from .models import News
from .service import send

load_dotenv()

@app.task
def send_email_every_1day(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for news in News.objects.filter(public_date=datetime.today().date()): # filter
        for user in User.objects.all():
            print(user.email)
            send_mail(news.header,
                      news.description,
                      'SibDoski-server@yandex.ru',
                      [user.email],
                      fail_silently=False,
                      )


@app.task
def get_weather_info():
    for place in Place.objects.all():
        appid = os.getenv('API_WEATHER_KEY')
        lon = place.lon
        lat = place.lat
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&units=metric&lon={lon}&appid={appid}'
        res = requests.get(url.format(lat, lon)).json()
        Weather.objects.create(temperature=res["main"]["temp"], pressure=res["main"]["pressure"],
                               windy_speed=res["wind"]["speed"], place=place, date=datetime.today().date())
