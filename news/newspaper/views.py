from django.shortcuts import redirect
from djoser import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from newspaper.models import News
from newspaper.serializers import NewsSerializers

from .tasks import send_email_every_1day


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    permission_classes = [permissions.permissions.IsAuthenticated]


class ContactView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    permission_classes = [permissions.permissions.IsAuthenticated]

    @action(methods=["get"], url_path='send-email', detail=False)
    def file_info(self, request):
        send_email_every_1day.delay()
        return redirect('/news')
