from django.shortcuts import render

from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    data = [{"title": movie.title, "description": movie.description, "producer": movie.producer, "duration": movie.duration} for movie in movies]
    return JsonResponse(data, safe=False)

def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    data = {"title": movie.title, "description": movie.description, "producer": movie.producer, "duration": movie.duration}
    return JsonResponse(data)
