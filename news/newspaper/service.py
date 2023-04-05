from django.core.mail import send_mail


def send(user_email):
    send_mail('QWERTY',
              'QWERTYQWERTY',
              'SibDoski-server@yandex.ru',
              [user_email],
              fail_silently=False,
              )