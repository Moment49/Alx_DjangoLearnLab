from typing import Any
from django.shortcuts import render
from .models import Library, Book
from django.views.generic.list import ListView

# Create your views here.
# Function based View
def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)

# Class Based View
class LibraryBookListView(ListView):
    model = Library
    context_object_name = "library"
    template_name = "relationship_app/library_detail.html"
    queryset = Library.objects.get(name="tech library")
    
    def get_context_data(self, **kwargs: Any):
        context_data = super().get_context_data(**kwargs)

        context_data['publication_year'] = "2024"
      
        return context_data
    