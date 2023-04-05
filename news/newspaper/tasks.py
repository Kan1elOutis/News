from news.celery import app

from .service import send


@app.task
def send_email_every_1day(user_email):
    send(user_email)
