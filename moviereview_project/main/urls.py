from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name = "home"),
    path('my_reviews/', views.my_reviews, name = "my_reviews"),
    path('movie/<int:movie_id>', views.movie, name = "movie"),
]