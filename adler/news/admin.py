from django.contrib import admin
from django.utils.html import mark_safe
from django.conf import settings

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'show', 'pub_date', 'news_image', )
    fields = ('pub_date', 'title', 'show', 'text', 'photo', )

    def news_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{settings.MEDIA_URL}{obj.photo}"' 
                             f'height="50px">')
        else:
            return ''
