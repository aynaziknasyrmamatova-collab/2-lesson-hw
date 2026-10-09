from django.urls import path
from .views import BookDetailView,BookListCreateView
urlpatterns=[
    path('book/',BookListCreateView.as_view(),name='book'),
    path('book/<int:pk>',BookDetailView.as_view(),name='book-detail')
]