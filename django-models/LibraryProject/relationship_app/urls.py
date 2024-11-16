from django.urls import path
from . import views


urlpatterns = [
    path('list-books/', views.list_books, name="list-books"),
    path('library-books/', views.LibraryBookListView.as_view(), name="library-books"),
]