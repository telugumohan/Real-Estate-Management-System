from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('/blog', views.blog, name='blog'),
    path('/about', views.about, name='about')
]
