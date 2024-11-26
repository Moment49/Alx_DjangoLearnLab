from django.urls import path
from .views import list_books, LibraryDetailView, LoginView, LogoutView, home, admin_view, member_view, librarian_view
from . import views



urlpatterns = [
    path('list-books/', list_books, name="list-books"),
    path('library-books/<int:pk>', LibraryDetailView.as_view(), name="library-books"),
    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
    path('', home, name="home"),
    path('admin_view/', admin_view, name='admin_view'),
    path('member_view/', member_view, name='member_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('delete_book/<int:id>', views.delete_book, name="delete_book"),
    path('edit_book/<int:id>', views.edit_book, name="edit_book"),
]