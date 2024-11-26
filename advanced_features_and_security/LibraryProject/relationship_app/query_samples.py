from relationship_app.models import Book, Author, Librarian, Library


# Query all books by a specific author.
try:
    author_name = "Jack Miller"
    author = Author.objects.get(name=author_name)
    author_books = Book.objects.filter(author=author)
    print(f"The list of books belonging to the author {author} are: {author_books}")
except Author.DoesNotExist:
    print("No author found")


# List all books in a library.
try:
    library_name = "tech library"
    lib = Library.objects.get(name=library_name)
    print(f"The set of books in the library are: {lib.books.all()}")
except Library.DoesNotExist:
    print("No library found")

# Retrieve the librarian for a library
try:
    library_name = "tech library"
    lib = Library.objects.filter(name=library_name).first()
    librarian = Librarian.objects.get(library=lib).first()
    print(f"The Library for the Library {lib} is {librarian}")
except Librarian.DoesNotExist:
    print("No Librarian Found")


