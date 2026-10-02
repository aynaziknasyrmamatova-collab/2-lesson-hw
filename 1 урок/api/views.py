from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
class Hell(APIView):
    def get(self,request):
        return Response({
            "message": "APIView in rest framework like this!"
        })
class People(APIView):
    def get(self,request):
        return Response({
            'name': 'Ainazik',
            'city':'Osh',
            "age" :"16"

        })
@api_view(["GET"])
def people(request):
    return Response({
        "message": "APIView in restframework decorator function"
    })
@api_view(['GET'])
def hello_api(request):
    return Response({
        "message": "APIView in restframework function style decorators!"
        })
