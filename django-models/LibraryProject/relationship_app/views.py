from typing import Any
from django.shortcuts import render, redirect
from .models import Library, Book, UserProfile
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import RegiesterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

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
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

class LoginView(LoginView):
    template_name = 'registration/login.html'
    next_page = 'home'


class LogoutView(LogoutView):
    template_name = 'registration/logout.html'


def home(request):
    return render(request, 'relationship_app/home.html')


def is_admin(user):
    user = UserProfile.objects.get(user=user)
    if user.roles != "Admin":
        return False
    return user

def is_librarian(user):
    user = UserProfile.objects.get(user=user)
    if user.roles == "Librarian":
        return user
def is_member(user):
    user = UserProfile.objects.get(user=user)
    if user.roles == "Member":
        return user

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

    