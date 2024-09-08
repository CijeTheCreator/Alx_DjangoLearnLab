from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author

class BookAPITests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book_data = {
            "title": "Test Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        url = reverse('book-create')
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_get_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_book(self):
        url = reverse('book-update', kwargs={'pk': self.book.id})
        updated_data = {"title": "Updated Book Title", "publication_year": 2022, "author": self.author.id}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book Title")

    def test_delete_book(self):
        url = reverse('book-delete', kwargs={'pk': self.book.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BookQueryTests(APITestCase):
    def setUp(self):
        self.author1 = Author.objects.create(name="Author A")
        self.author2 = Author.objects.create(name="Author B")
        Book.objects.create(title="Book 1", publication_year=2020, author=self.author1)
        Book.objects.create(title="Book 2", publication_year=2021, author=self.author2)

    def test_filter_books_by_author(self):
        url = reverse('book-list') + '?author__name=Author A'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Book 1'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book 1')


from rest_framework.test import APIClient

class BookPermissionTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="Test Author")
        self.book_data = {
            "title": "Test Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        self.book = Book.objects.create(**self.book_data)
        self.url = reverse('book-create')

    def test_unauthenticated_create_book(self):
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
