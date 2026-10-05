from django.contrib import admin
from django.urls import path,include
from .views import CarView
urlpatters=[
    path('car/',CarView.as_view()),
    path('',include('serializer.url'))
]