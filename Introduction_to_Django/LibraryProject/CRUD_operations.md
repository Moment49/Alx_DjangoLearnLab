# Create 
# Python Command to Create a book : 
# book1 = Book(title=“1984”m author=“George Orwell”, publication year=1949)
# book1.save()
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
# Retrieve and display all attributes of the book you just created.
# Python Command to Display all books : 
# books = Book.objects.all()
# for book in books:
#    print(book)
# comment: books successfully retrieved
