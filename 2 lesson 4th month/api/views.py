from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Books
class BookListApi(ListView):
    model=Books
    template_name='Lesson2/book_list.html'
    context_object_name='books'
class BookDetailApi(DetailView):
    model=Books
    template_name='Lesson2/book_list.html'
    context_object_name='book'

