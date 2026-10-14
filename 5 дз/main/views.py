from django.shortcuts import render
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet

from .models import Visitors, Zone
from .serializers import VisitorsSerializer, ZoneSerializer
# Create your views here.
class ZoneViewSet(ModelViewSet):
	queryset = Zone.objects.all()
	serializer_class = ZoneSerializer
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ["location"]
	search_fields = ["name", "description"]
	ordering_fields = ["name", "location", "created_at"]


class VisitorsViewSet(ModelViewSet):
	queryset = Visitors.objects.select_related("zone").all()
	serializer_class = VisitorsSerializer
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ["is_allowed", "zone"]
	search_fields = ["full_name"]
	ordering_fields = ["full_name", "is_allowed", "created_at"]

