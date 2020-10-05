from ckeditor.widgets import CKEditorWidget

from django import forms
from django.contrib import admin
from django.utils.html import mark_safe
from django.conf import settings

from .models import News


class TextEditorForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = TextEditorForm
    list_display = ('title', 'show', 'pub_date', 'news_image', )
    fields = ('pub_date', 'title', 'show', 'text', 'photo', )

    def news_image(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{settings.MEDIA_URL}{obj.photo}"' 
                             f'height="50px">')
        else:
            return ''
