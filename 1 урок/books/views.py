from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from .models import Books
from .seriliazer import BooksSerializer
class BookListApi(APIView):
    def get(self,request):
        books=Books.objects.all()
        serializer=BooksSerializer(books,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)