from django import forms

class ExampleForm(forms.Form):
    search_book = forms.CharField(label="Search books")