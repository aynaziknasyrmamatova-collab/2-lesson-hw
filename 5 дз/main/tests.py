from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Visitors, Zone


class ZoneApiTests(APITestCase):
	def test_zone_list_is_paginated_and_includes_visitor_count(self):
		zone = Zone.objects.create(
			name="Старая станция",
			location="Алматы",
			coordinates="43.2389, 76.8897",
			description="Заброшенная железнодорожная станция",
		)
		Visitors.objects.create(
			zone=zone,
			full_name="Иван Петров",
			info="Исследователь",
			is_allowed=True,
		)

		response = self.client.get(reverse("zone-list"))

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data["count"], 1)
		self.assertEqual(response.data["results"][0]["visitors_count"], 1)


class VisitorsApiTests(APITestCase):
	def test_visitors_can_be_filtered_and_searched(self):
		zone = Zone.objects.create(
			name="Старая станция",
			location="Алматы",
			coordinates="43.2389, 76.8897",
			description="Заброшенная железнодорожная станция",
		)
		Visitors.objects.create(
			zone=zone,
			full_name="Иван Петров",
			info="Исследователь",
			is_allowed=True,
		)
		Visitors.objects.create(
			zone=zone,
			full_name="Анна Смирнова",
			info="Фотограф",
			is_allowed=False,
		)

		response = self.client.get(
			reverse("visitors-list"), {"is_allowed": "true", "search": "Иван"}
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data["count"], 1)
		self.assertEqual(response.data["results"][0]["full_name"], "Иван Петров")


