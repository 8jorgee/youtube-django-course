from django.http import HttpResponse
from django.shortcuts import render

def movies(request):
    return render(request, 'movies/movies.html', {'name': 'Movies'})


def home(request):
    return HttpResponse("Home page")
