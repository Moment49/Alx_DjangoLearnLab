from django.urls import path
from .views import list_books, LibraryDetailView, register_view

urlpatterns = [
    path('list-books/', list_books, name="list-books"),
    path('library-books/<int:pk>', LibraryDetailView.as_view(), name="library-books"),
    path('register/', register_view, name="register"),
]