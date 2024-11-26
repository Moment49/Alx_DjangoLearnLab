from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings



# Create your models here.
# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, date_of_birth, password=None):
#         if not username:
#             raise ValueError("username is required")
#         if not password:
#             raise ValueError("password is required")
#         if not date_of_birth:
#             raise ValueError("Date of birth is required")
#         # create the user obj
#         user = self.model(date_of_birth=date_of_birth, username=username)

#         user.set_password(password)
#         user.save(using=self._db)

#         return user
    
#     def create_superuser(self, username, date_of_birth, password=None):
#         user = self.create_user(username=username,date_of_birth=date_of_birth, password=password)
#         user.is_staff = True
#         user.is_admin = True
#         user.is_active = True
#         user.is_superuser = True

#         user.save(using=self._db)

#         return user
            


# class CustomUser(AbstractUser):
#     profile_photo = models.ImageField(upload_to='uploads/', blank=True, null=True)
#     date_of_birth = models.DateField(null=True, blank=True)

#     objects = CustomUserManager()
#     REQUIRED_FIELDS = ['date_of_birth']

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
    


