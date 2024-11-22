from django.contrib import admin
from .models import UserProfile, Book

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Book)
