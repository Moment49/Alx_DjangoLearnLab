from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('view/', views.view, name='view'),
    path('book_list/', views.book_list, name='book_list'),
]