from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('program/', views.program, name='program'),
    path('category/', views.category, name='category'),
]
