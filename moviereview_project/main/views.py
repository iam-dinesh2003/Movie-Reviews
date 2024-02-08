from django.shortcuts import render, redirect
from django.db.models import Avg
from django.contrib.auth.models import User
from .models import *

def home(request):
    movies = Movie.objects.all()
    return render(request, 'main/home.html', {'movies': movies})

def my_reviews(request):
    user = request.user
    if user.is_authenticated:
        reviews = Review.objects.filter(user=user)
        return render(request,'main/my_reviews.html', {'reviews': reviews})
    return render(request, 'main/my_reviews.html')

def movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    already_exists = False
    user = request.user
    if user.is_authenticated:
        already_exists = Review.objects.filter(user=user, movie=movie).exists()
    if request.method == 'POST' and user.is_authenticated:
        if already_exists:
            return redirect('main:movie', movie_id)
        review = request.POST['review']
        rating = request.POST['rating']
        review = Review(movie=movie, user=user, user_rating=rating, user_review=review)
        review.save()
        return redirect('main:movie', movie_id)
    movie = Movie.objects.get(id=movie_id)
    reviews = Review.objects.filter(movie=movie)
    average_rating = reviews.aggregate(Avg('user_rating'))['user_rating__avg']
    if (average_rating is not None):
        movie.average_rating = average_rating
        movie.save()
        no_rating = False
    else:
        no_rating = True
    return render(request, 'main/movie.html', {'movie': movie, 'no_rating': no_rating, 'reviews': reviews, 'already_exists': already_exists})