from django.db import models

# import built in model from django
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def no_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_ratings(self):
        sum_ratings = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum_ratings += rating.stars
        if len(ratings):
            avg = sum_ratings / len(ratings)
            return avg
        else:
            return 'no rating available'


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(5)])
    class Meta:
        # each movie can be rated once by a user
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
