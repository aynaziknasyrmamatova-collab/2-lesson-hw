from django.shortcuts import render
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializers

class TaskView(APIView):
    def get(self,request):
        tasks_data=cache.get("tasks")
        if tasks_data is not None:
            return Response(tasks_data)
        tasks=Task.objects.all()
        serializer=TaskSerializers(tasks,many=True)
        tasks_data=serializer.data
        cache.set("tasks",tasks_data,60)
        return Response(tasks_data)
    def post(self,request):
        serializer=TaskSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cache.delete("tasks")
        return self.response(serializer.data,status=status.HTTP_201_CREATED)
    
# Create your views here.
