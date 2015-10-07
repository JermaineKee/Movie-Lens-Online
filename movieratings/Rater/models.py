from django.db import models

# Create your models here.


class Rater(models.Model):
    rater_id = models.PositiveIntegerField()

    def __str__(self):
        return 'Rater ID: {}'.format(self.rater_id)


class Rating(models.Model):
    user = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'user {} gives {} a {}'.format(self.user, self.movie, self.rating)


class Movie(models.Model):
    title = models.CharField(max_length=255)


    def __str__(self):
        return '{}'.format(self.title)
