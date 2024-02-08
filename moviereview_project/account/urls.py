from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "account"

urlpatterns = [
    path('login/', views.loginn, name = "login"),
    path('logoutt/', views.logoutt, name = "logout"),
    path('register/', views.register, name = "register"),
]