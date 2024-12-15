from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Post, Comment
import re
from django.core.exceptions import ValidationError

class UserRegistration(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {field: None for field in fields}
        widgets = {
            "username": forms.TextInput(attrs={'placeholder': 'Username'}),
            "first_name": forms.TextInput(attrs={'placeholder': 'First Name'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Last Name'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(UserRegistration, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ''

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_img', 'bio', 'date_of_birth', 'age']

class UserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", 'tags']
    
    def save(self, commit=True):
        instance = super(PostForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance
    
    def clean(self):
        super(PostForm, self).clean()
        title = self.cleaned_data['title']
        regex = re.compile('[0-9@_!#$%^&*()<>?/\|}{~:]')

        if len(title) > 200 or regex.search(title) != None:
             raise ValidationError("Title must not contain special characters or numbers and should be less than 200")
        else:
            print("Title is valid")
       
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']