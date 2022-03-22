from django import forms
from .models import *

class BookForm(forms.Form):
    class Meta:
        model = Book
        fileds = ('name', 'image')