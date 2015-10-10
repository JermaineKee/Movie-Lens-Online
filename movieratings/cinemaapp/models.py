from django.db import models
# Create your models here.


class Rater(models.Model):

    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'F'),
    )

    age = models.PositiveSmallIntegerField()
    occupation = models.CharField(max_length=40)
    gender = model.CharField(max_length=1, choices=GENDER_CHOICES)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return (self.id)


class Movie(models.Model):
    title = models.CharFields(max_length=255)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('rating'))['rating__avg']

    def __str__(self):
        return '{}'.format(self.title)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    stars = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'Rater {}, Title: {}, Rating: {}'.format
        (self.rater, self.movie, self.rating)
