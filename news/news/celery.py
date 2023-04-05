import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')

app = Celery('news')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-email-every-1-min':{
        'task': 'newspaper.tasks.send_email_every_1day',
        'schedule': crontab(minute='*/1'),
    }
}
