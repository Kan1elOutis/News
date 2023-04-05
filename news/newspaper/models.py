import os
from io import BytesIO

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import models
from PIL import Image


class News(models.Model):
    header = models.CharField(max_length=128)
    main_image = models.ImageField(upload_to='media/photos')
    preview_image = models.ImageField(upload_to='media/photos_low', null=True, blank=True)
    description = models.TextField(null=False, blank=False)
    public_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.make_thumbnail():
            raise Exception('Could not create thumbnail - is the file type valid?')

        super(News, self).save(*args, **kwargs)

    def make_thumbnail(self):
        image = Image.open(self.main_image)
        image.thumbnail((200, 200))

        thumb_name, thumb_extension = os.path.splitext(self.main_image.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False

        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        self.preview_image.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return f'{self.header}'
