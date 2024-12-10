from django.db import models

# Create your models here.

class Author(models.Model):
    """This is an author model with just a single field "name" which is used to hold the author_name"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    """This is a book model with fields which repr. the book and a foreign key referencing the author of the book"""
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} {self.publication_year}"
