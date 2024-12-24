from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password):
        ...

    def create_superuser(self, email, password):
        ...


class User(AbstractUser):
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=False)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='uploads/', blank=True, null=True)
    followers = models.ManyToManyField("self", symmetrical=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

class UserProfile(models.Model):
    user = models.OneToOneField(User)