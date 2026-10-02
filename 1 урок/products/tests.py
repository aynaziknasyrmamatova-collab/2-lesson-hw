from django.test import TestCase
from rest_framework.test import APIClient

from .models import Product


class ProductListCreateAPITest(TestCase):
	def test_get_products_returns_all_products(self):
		Product.objects.create(
			title="Наушники Sony WH-1000XM5",
			description="Беспроводные наушники с шумоподавлением",
			price="34990.00",
			quantity=5,
		)

		response = APIClient().get("/api/v1/products/")

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.data), 1)
		self.assertEqual(response.data[0]["title"], "Наушники Sony WH-1000XM5")
		self.assertEqual(response.data[0]["price"], "34990.00")
		self.assertEqual(response.data[0]["quantity"], 5)
