from django import forms
import re
from django.core.exceptions import ValidationError

def search_title_no_number(value):
    regex = re.compile('[0-9 @_!#$%^&*()<>?/\|}{~:]')
    if regex.search(value) == None:
        print("title is good")
    else:
        raise ValidationError("Title must not contain special characters or numbers")

class ExampleForm(forms.Form):
    title = forms.CharField(label="Search books", max_length=100, validators=[search_title_no_number])