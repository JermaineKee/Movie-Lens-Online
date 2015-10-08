from django.db import models

# Create your models here.


class Rater(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    NORESPONSE = 'X'
    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'F'),
        (OTHER, 'O'),
        (NORESPONSE, 'X'),
        )

    age = models.PositiveSmallIntegerField()
    occupation = models.CharField(max_length=40)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='X')
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return (self.id)


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.title)


class Rating(models.Model):
    user = models.ForeignKey(Rater)
    title = models.ForeignKey(Movie)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'Rater {}, Title: {} ,Rating: {}'.format(self.user, self.movie, self.rating)


def load_ml_data():
    import csv
    import json
    import re

    users = []

    with open('ml-1m/movies.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='\t')

        for row in reader:
            user = {
                'fields': {
                    'gender': row['Gender'],
                    'age': row['Age'],
                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'ratings.Rater',
                'pk': int(row['UserID']),
            }

            users.append(user)

        with open('user.json', 'w') as f:
            f.write(json.dumps(users))

        print(json.dumps(users, sort_keys=True, indent=4, separators=(',', ':')))
