from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings



# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        permissions = (("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
            )

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ROLES = (
        ("Admin", 'Admin'),
        ("Librarian", 'Librarian'),
        ("Member", 'Member'),
    )
    roles = models.CharField(max_length=100, choices=ROLES, default='Member')

    def __str__(self) -> str:
        return f"{self.user.username}'s Profile and {self.roles}"
    

