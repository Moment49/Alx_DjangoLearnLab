from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(label="Search books", max_length=100)