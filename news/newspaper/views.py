from django.core.mail import send_mail
from django.shortcuts import render, redirect
from djoser import permissions
from djoser.serializers import User
from rest_framework.viewsets import ModelViewSet

from newspaper.models import News
from newspaper.serializers import NewsSerializers
from .service import send
from .tasks import send_email_every_1day


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    permission_classes = [permissions.permissions.IsAuthenticated]


class ContactView(ModelViewSet):
    queryset = User.objects.all()

    email = str(User.email)
    success_url = '/'
    permission_classes = [permissions.permissions.IsAuthenticated]

    send_email_every_1day.delay(user_email=email)


def send_email(request):
    email = str(User.email)
    send_mail('QWERTY',
              'QWERTYQWERTY',
              'SibDoski-server@yandex.ru',
              [email],
              fail_silently=False,
              )
    # send_email_every_1day.delay(user_email=email)
    return redirect('/news')
