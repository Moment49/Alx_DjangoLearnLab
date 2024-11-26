from django.contrib import admin
from .models import UserProfile, Book
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Book)

