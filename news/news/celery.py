import os

from celery import Celery
from celery.schedules import crontab
from constance import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')

app = Celery('news')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-email-every-1-min': {
        'task': 'newspaper.tasks.send_beat_email',
        'schedule': crontab(minute=config.EMAIL_SEND_HOUR,
                            hour=config.EMAIL_SEND_MINUTES),
    },
    'save_weather_info': {
        'task': 'newspaper.tasks.get_weather_info',
        'schedule': crontab(minute=config.EMAIL_SEND_MINUTES,
                            hour=config.WEATHER_GET_HOUR),
    }
}
