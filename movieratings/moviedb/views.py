from django.shortcuts import render


# Create your views here.
def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request,
                   '.html',
                   {'movie': movie})
