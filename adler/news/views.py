from django.shortcuts import render
from .models import News


def news(request):
    context = {
        'news': News.objects.all()
    }
    return render(request, 'post-page.html', context)
