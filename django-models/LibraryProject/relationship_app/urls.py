from django.urls import path
from .views import list_books, LibraryDetailView, LoginView, LogoutView, home
from . import views



urlpatterns = [
    path('list-books/', list_books, name="list-books"),
    path('library-books/<int:pk>', LibraryDetailView.as_view(), name="library-books"),
    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', home, name="home"),
]