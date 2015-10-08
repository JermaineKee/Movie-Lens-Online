
from django.contrib import admin

# Register your models here.
from .models import Movie, Rater, Rating


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'rating']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Movie)
admin.site.register(Rater, RaterAdmin)
admin.site.register(Rating)
