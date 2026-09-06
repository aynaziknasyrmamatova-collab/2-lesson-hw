from django.urls import path
from .views import MovieDetailApi, MovieListApi
urlpatterns=[
    path('',MovieListApi.as_view(),name='movie_list'),
    path('<int:pk>/',MovieDetailApi.as_view(),name="movie_detail"),
]