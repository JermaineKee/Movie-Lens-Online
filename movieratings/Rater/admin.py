from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Movie, Rater, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['rater_id']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['rater_id', 'movie', 'rating']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_name', 'movie_id']






admin.site.register(Movie, MovieAdmin)
admin.site.register(Rater, RaterAdmin)
admin.site.register(Rating, RatingAdmin)
