from django.shortcuts import render
from .models import News


def news(request):
    context = {
        'news': News.objects.all()
    }
    print(context)
    return render(request, 'post-page.html', context)
