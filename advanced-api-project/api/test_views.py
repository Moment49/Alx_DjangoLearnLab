from django.test import TestCase, Client
from .models import Book, Author
from django.urls import reverse

# Create your tests here.
class BookModels(TestCase):
    def setUp(self):
        """Set up for each test that will run before each test"""
        self.author = Author.objects.create(name="john")
        self.book = Book.objects.create(title="wonderland", publication_year=2023, author=self.author)
    def test_model_book(self):
        self.assertEqual(str(self.book), 'wonderland 2023')
        self.assertTrue(isinstance(self.book, Book))
    
class TestListBook(TestCase):
        def test_list_book(self):
            c = Client()
            response = self.client.get(reverse('list_books'), {"author":{"name":"john"}, "title":"wonderland","publication_year":2023})
            self.assertEqual(response.status_code, 200)

class TestCreateBook(TestCase):
        def test_create_book(self):
            c = Client()
            response = self.client.post(reverse('book_create'), {"author":{"name":"john"}, "title":"wonderland","publication_year":2023})
            self.assertEqual(response.status_code, 200)

class TestDeleteBook(TestCase):
        def test_delete_book(self):
            c = Client()
            response = self.client.delete(reverse('delete_book', args=[0]))
            self.assertEqual(response.status_code, 204)

