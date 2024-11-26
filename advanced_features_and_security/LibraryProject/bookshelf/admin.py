from django.contrib import admin
from .models import Book
from .models import Book, CustomUser
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_year']
    list_filter = ['author', 'title', 'publication_year']
    search_fields = ['title', 'author']

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["username", "date_of_birth", "password", "profile_photo"]

class CustomUserAdmin(BaseUserAdmin):
    form = MyUserChangeForm
    list_display = ["date_of_birth", "profile_photo", "username"]

    fieldsets = [
        (None, {"fields": ["username", "password"]}),
        ("Personal info", {"fields": ["date_of_birth", "profile_photo"]}),
        
    ]

    # Uses this field set when creating the user
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username", "date_of_birth", "password1", "password2", "profile_photo"],
            },
        ),
    ]
    


admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
