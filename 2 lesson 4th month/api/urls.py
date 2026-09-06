from django.urls import path
from .views import BookDetailApi, BookListApi
urlpatterns=[
    path('', BookListApi.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailApi.as_view(), name='book_detail'),
]