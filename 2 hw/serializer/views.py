from django.shortcuts import render
from django.core.cache import cache
from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import ModelSerializers
class CarView(APIView):
    def get(self,request):
        cars_data=cache.get("cars")
        if cars_data is not None:
            return Response(cars_data)
        cars=Car.objects.all()
        serializer=ModelSerializers(cars,many=True)
        cars_data=serializer.data
        cache.set("cars",cars_data,60)
        return Response(cars_data)
    def post(self,request):
        serializer=ModelSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.delete("cars")
        return self.response(serializer.data,status=status.HTTP_201_CREATED)

# Create your views here.
