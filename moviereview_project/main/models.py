from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    movie_name = models.CharField(max_length=255)
    movie_director = models.CharField(max_length=255)
    average_rating = models.FloatField(default=-1, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    movie_src = models.CharField(max_length=255)

    def __str__(self):
        return self.movie_name

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_rating = models.FloatField()
    user_review = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s review for {self.movie.movie_name}"