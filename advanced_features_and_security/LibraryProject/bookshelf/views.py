from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book


# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/books_list.html", {"booka": books})

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