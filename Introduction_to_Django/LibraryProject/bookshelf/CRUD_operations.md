# Create 
# Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.
# Python Command to Create a book : 
# Book.objects.create(title=“1984”m author=“George Orwell”, publication year=1949)
# comment: books successfully created

# Update
# Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.
# Command to update the book in the shelf:
# book = Book.objects.all().get(title="1984")
# book.title = "Nineteen Eighty-Four
# book.save()
# Comment: book succesfully updated

# Delete
# Delete the book you created and confirm the deletion by trying to retrieve all books again.
# Command to delete the book in the shelf:
# book_del = Book.objects.all().get(id=3)
# book_del.delete()
# Expected Comment:  (1, {'bookshelf.Book': 1}) successfully deleted

# Retrieve
# Delete the book you created and confirm the deletion by trying to retrieve all books again.
# Command to delete the book in the shelf:
# from bookshelf.models import Book
# book= Book.objects.all().get(id=3)
# book.delete()
# comment: books successfully retrieved
