from django.test import TestCase
from rest_framework.test import APIClient

from .models import Book


class BookApiTests(TestCase):
	def setUp(self):
		self.client = APIClient()

	def test_book_crud(self):
		list_response = self.client.get('/books/')
		self.assertEqual(list_response.status_code, 200)
		self.assertEqual(list_response.data, [])

		create_response = self.client.post(
			'/books/',
			{'title': 'The Hobbit', 'author': 'J. R. R. Tolkien'},
			format='json',
		)
		self.assertEqual(create_response.status_code, 201)
		book_id = create_response.data['id']

		detail_response = self.client.get(f'/books/{book_id}/')
		self.assertEqual(detail_response.status_code, 200)
		self.assertEqual(detail_response.data['title'], 'The Hobbit')

		update_response = self.client.put(
			f'/books/{book_id}/',
			{'title': 'The Hobbit: Revised', 'author': 'J. R. R. Tolkien'},
			format='json',
		)
		self.assertEqual(update_response.status_code, 200)
		self.assertEqual(update_response.data['title'], 'The Hobbit: Revised')

		delete_response = self.client.delete(f'/books/{book_id}/')
		self.assertEqual(delete_response.status_code, 204)
		self.assertFalse(Book.objects.filter(pk=book_id).exists())

	def test_create_book_rejects_missing_fields(self):
		response = self.client.post('/books/', {}, format='json')

		self.assertEqual(response.status_code, 400)
		self.assertEqual(Book.objects.count(), 0)
