from relationship_app.models import Book, Author, Librarian, Library


# Query all books by a specific author.
try:
    author_name = Author.objects.filter(name="Jack Miller").first()
    author_books = Book.objects.filter(author__name=author_name)
    print(f"The list of books belonging to the author {author_name} are: {author_books}")
except Author.DoesNotExist:
    print("No author found")


# List all books in a library.
try:
    lib = Library.objects.get(pk=4)
    print(f"The set of books in the library are: {lib.books.all()}")
except Library.DoesNotExist:
    print("No library found")

# Retrieve the librarian for a library
try:
    lib = Library.objects.filter(name="tech library").first()
    librarian = Librarian.objects.filter(library=lib).first()
    print(f"The Library for the Library {lib} is {librarian}")
except Librarian.DoesNotExist:
    print("No Librarian Found")


