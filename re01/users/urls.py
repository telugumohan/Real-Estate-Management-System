from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('user-register/', views.signup_view, name="user_register"),
    path('user-login/', views.login_view, name="user_login"),
    path('user-logout/', views.logout_view, name="user_logout"),
]
