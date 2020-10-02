from django.shortcuts import render
from django.template import loader


def index(request):
    some_list = [f'Some good text {i}' for i in range(100)]
    context = {'some_list': some_list}
    return render(request, 'home-page.html', context)


def program(request):
    return render(request, 'post-page.html')


def category(request):
    return render(request, 'category-page.html')

