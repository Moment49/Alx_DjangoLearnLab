from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('list-books/', list_books, name="list-books"),
    path('library-books/', LibraryDetailView.as_view(), name="library-books"),
]