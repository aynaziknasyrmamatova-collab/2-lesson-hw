from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache

from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer

CACHE_KEY_CATEGORIES = 'categories'
from rest_framework import mixins,generics
from .serializer import TaskSerializer
from django.core.cache import cache


# Create your views here.
CACHE_KEY_CATEGORIES='categories'
CACHE_TTL=60
class CategoryListCreateView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    genrics.GenericAPIView
):
    
(queryset=Category.objects.all()
    serializer_class=CategorySerializer
    def get_queryset(Self):
        queryset=Category.objects.all()
        q=self.request.query_params.get('q')
        if q:
            queryset=queryset.filter(name_incontains=q)
        return queryset #фильтр по параметрам
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs) #
    def post(self,request,*args,**kwargs):
            return self.create(request,*args,**kwargs)
class CategoryDetailView(
     mixins.RetriveModelMixin,
     mixins.UpdateModelMixin,
     mixins.DestroyModelMixin,
    generics.GenericAPIView
)
    def get_queryset(Self):
        queryset=Category.objects.all()
        q=self.request.query_params.get('q')
    if q:
        queryset=queryset.filter(name_incontains=q)
        return queryset #фильтр по параметрам
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs) #
    def patch(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
