from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from api.models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()

        # Create an author and some books
        self.author = Author.objects.create(name='Author One')
        self.book1 = Book.objects.create(title='Book One', author=self.author, publication_year=2020)
        self.book2 = Book.objects.create(title='Book Two', author=self.author, publication_year=2021)

        # Endpoints
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book1.pk})

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book One')

    def test_create_book_requires_authentication(self):
        # Unauthenticated request
        data = {
            'title': 'Book Three',
            'author': self.author.id,
            'publication_year': 2022
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Book Three',
            'author': self.author.id,
            'publication_year': 2022
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Updated Book One',
            'author': self.author.id,
            'publication_year': 2023
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book One')

    def test_delete_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    def test_filter_books_by_title(self):
        response = self.client.get(f"{self.list_url}?title=Book One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_publication_year(self):
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))

    def test_permissions_for_update(self):
        # Unauthenticated request should fail
        data = {
            'title': 'Unauthorized Update',
            'author': self.author.id,
            'publication_year': 2025
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_permissions_for_delete(self):
        # Unauthenticated request should fail
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

def setUp(self):
    self.user = User.objects.create_user(username='testuser', password='testpass')
    self.client.login(username='testuser', password='testpass')

