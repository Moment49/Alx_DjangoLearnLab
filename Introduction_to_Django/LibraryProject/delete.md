# Delete the book you created and confirm the deletion by trying to retrieve all books again.
# Command to delete the book in the shelf:
# book_del = Book.objects.all().get(id=3)
# book_del.delete()
# Expected Comment:  (1, {'bookshelf.Book': 1})