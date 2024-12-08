from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


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
        fields = ['profile_img', 'bio', 'date_of_birth', 'age', 'user']
