from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title} {self.author} {self.publication_year}"
    
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, date_of_birth, password=None):
        if not username:
            raise ValueError("username is required")
        if not password:
            raise ValueError("password is required")
        if not date_of_birth:
            raise ValueError("Date of birth is required")
        # create the user obj
        user = self.model(date_of_birth=date_of_birth, username=username)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, date_of_birth, password=None):
        user = self.create_user(username=username,date_of_birth=date_of_birth, password=password)
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True

        user.save(using=self._db)

        return user
            


class CustomUser(AbstractUser):
    profile_photo = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)

    objects = CustomUserManager()
    REQUIRED_FIELDS = ['date_of_birth']