from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, profile_picture=None, bio=None, username=None):
        if email is None:
            raise ValueError("Email is required")
        if password is None:
            raise ValueError("Password is required")
        # if profile_picture is None:
        #     raise ValueError("profile_picture is required")
        user = self.model(email=self.normalize_email(email),profile_picture=profile_picture, bio=bio, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=False, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='uploads/', blank=True, null=True)
    following = models.ManyToManyField("self", symmetrical=False, related_name="user_followers")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f"{self.user}"