from django.shortcuts import render
from django.template import loader


def index(request):
    some_list = [f'Some good text {i}' for i in range(10)]
    context = {'some_list': some_list}
    return render(request, 'index.html', context)


def program(request):
    return render(request, 'program.html')

