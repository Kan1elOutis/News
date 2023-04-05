from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from newspaper.models import News


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    list_display = ('header', 'main_image', 'preview_image', 'description', 'public_date', 'author')
    fields = ('header', 'main_image', 'preview_image', 'description', 'public_date', 'author')
    readonly_fields = ['preview_image']
    summer_note_fields = ('header', 'description')
