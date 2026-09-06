from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movies

class MovieListApi(ListView):
    model=Movies
    template_name='Lesson2/movie_list.html'
    context_object_name="movies"
class MovieDetailApi(DetailView):
    model=Movies
    template_name="Lesson2/movie_list.html"
    context_object_name="movies"

