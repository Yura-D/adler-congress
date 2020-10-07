from django.db import models
from django.utils import timezone


def upload_handler(instance, filename):
    return f'news/{timezone.now():%m-%d-%Y}__{filename}'


class News(models.Model):
    pub_date = models.DateTimeField('Published date', null=True, blank=True)
    title = models.CharField('News title', max_length=255)
    text = models.TextField('Content')
    show = models.BooleanField(default=True)

    class Meta:
        db_table = 'all_news'
        verbose_name_plural = "All news"
    
    def save(self, *args, **kwargs):
        if not self.pub_date:
            self.pub_date = timezone.now()
        super().save(*args, **kwargs)

    def get_preview(self):
        if len(self.text) >= 500:
            return self.text[:500] + ' ...'
        else:
            return self.text[:500]


class Image(models.Model):
    photo = models.ImageField(upload_to=upload_handler, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'images'
