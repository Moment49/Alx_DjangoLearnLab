from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm


# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/books_list.html", {"books": books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create(request):
    return render(request, "bookshelf/create.html")


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit(request, id):
    return render(request, "bookshelf/edit.html")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete(request, id):
    return render(request, "bookshelf/delete.html")

@permission_required('bookshelf.can_view', raise_exception=True)
def view(request):
    return render(request, "bookshelf/view.html")

def search_book(request): 
    search_books = Book.objects.none
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            search_books = Book.objects.filter(title__contains=title)
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {"form": form, "search_books": search_books})