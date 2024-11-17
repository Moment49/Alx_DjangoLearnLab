from typing import Any
from django.shortcuts import render
from .models import Library, Book
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# Function based View
def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)

# Class Based View
class LibraryDetailView(DetailView):
    # The model
    model = Library
    # This defines tthe object name that will be instatiated once the class is called(acessible to the template)
    context_object_name = "library"
    # Defines the path of the template to be rendered
    template_name = "relationship_app/library_detail.html"
    # This performs the query as an attribute of the class (can be overidden)
    # use queryset when you want to use the ListView
    # queryset = Library.objects.get(name="tech library")

     
    def get_context_data(self, **kwargs: Any):
        """This is to add more data context to the View"""
        context_data = super().get_context_data(**kwargs)
        context_data['publication_year'] = "2024"
        return context_data

# Register view
def register_view(request):
    form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
    