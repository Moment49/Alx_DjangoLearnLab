from rest_framework.test import APITestCase, URLPatternsTestCase
from .models import Book, Author
from django.urls import reverse, include, path
from rest_framework import status

# Create your tests here.
class BookModels(APITestCase):
    def setUp(self):
        # Setup test client (this is automatically handled by APITestCase)
        
        # Create an author to associate with books
        self.author = Author.objects.create(
            name="J.K. Rowling"
        )
        
        # Data for creating a book
        self.book_data = {
            'title': 'Harry Potter and the Philosopher\'s Stone',
            'publication_year': 2022,
            'author': {
                'name': self.author.name
            }
        }

        Book.objects.create(title=self.book_data['title'], 
                            publication_year=self.book_data['publication_year'], author=self.author)

        self.book_del = Book.objects.get(title=self.book_data['title'])
        print(self.book_del.id)
    def test_create_book(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('book_create')
        response = self.client.post(url, self.book_data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 201)

    def test_delete_book(self):
        """Delete a book """
        url = reverse('delete_book',  kwargs={'pk': self.book_del.id})
        response = self.client.delete(url,  format="json")
        print(response.data)
        self.assertEqual(response.status_code, 204)
