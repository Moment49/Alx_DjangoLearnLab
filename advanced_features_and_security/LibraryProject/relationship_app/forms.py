from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Book

class RegiesterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class AddBookForm(forms.Form):
    title = forms.CharField(label="Book title", max_length=150)
    author = forms.CharField(label= "Book author", max_length=100)

class EditBookForm(forms.Form):
    title = forms.CharField(label="Book title", max_length=150)
    author = forms.CharField(label= "Book author", max_length=100)
    