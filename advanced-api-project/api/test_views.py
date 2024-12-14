from rest_framework.test import APITestCase, APIClient
from .models import Book, Author
from django.contrib.auth.models import User
from django.urls import reverse, include, path
from rest_framework import status
from rest_framework.authtoken.models import Token

# Create your tests here.
class BookModels(APITestCase):
    def setUp(self):
        # Setup test client (this is automatically handled by APITestCase)

        # Create the user and Token and associate the token with user
        self.user = User.objects.create_user(username="john", password="secret")
        self.token = Token.objects.create(user=self.user)

        self.client.login(username=self.user.username, password=self.user.password)

        # User data to be sent to obtain the token
        self.user_data = {
            "username":"john",
            "password":"secret"
        }
        token = Token.objects.get(user__username='john')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

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

        # Get the book instance
        self.book = Book.objects.get(title=self.book_data['title'])

        # Data for updating the book
        self.book_data_update = {
            'title': 'Alice in wonderland',
            'publication_year':2021,
            'author':{
                'name':self.book.author.name
            }
        }
        self.book.publication_year = self.book_data_update['publication_year']
        self.book.title = self.book_data_update['title']

    def test_create_book(self):
        """
        Ensure we can create a new book object.
        """
        # Set the authorization header using the user's token
        token = Token.objects.get(user__username='john')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('book_create')
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_delete_book(self):
        """Delete a book """
        url = reverse('delete_book',  kwargs={'pk': self.book.id})
        response = self.client.delete(url,  format="json")
        self.assertEqual(response.status_code, 204)

    def test_update_book(self):
        url = reverse('update_book', kwargs={'pk':self.book.id})
        response = self.client.put(url, self.book_data_update, format="json")
        self.assertEqual(response.status_code, 200)
     

    def test_token_obtain(self):
        url = reverse('obtain-token')
        response = self.client.post(url, self.user_data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.data)
        