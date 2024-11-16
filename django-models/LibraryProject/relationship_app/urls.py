from django.urls import path
from . import views


urlpatterns = [
    path('list-books/', views.list_books, name="list-books"),
    path('library-books/', views.LibraryListView.as_view(), name="library-books"),
]