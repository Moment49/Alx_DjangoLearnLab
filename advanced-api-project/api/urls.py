from django.urls import path
from .views import CreateView, ListView, DetailView, DeleteView, UpdateView
from rest_framework.authtoken import views

urlpatterns = [
    path('books/create', CreateView.as_view(), name="book_create"),
    path('books/', ListView.as_view(), name="list_books"),
    path('books/<int:pk>', DetailView.as_view(), name="retrieve_book"),
    path('books/update/<int:pk>', UpdateView.as_view(), name="update_book"),
    path('books/delete/<int:pk>', DeleteView.as_view(), name="delete_book"),
    path('atouth_ken/', views.obtain_auth_token, name="obtain-token")
]