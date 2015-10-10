from django.contrib import admin
from .models import Movie, Rater, Rating

# Register your models here.


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'gender', 'occupation', 'zipcode']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'rater', 'movie', 'stars']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']
