from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request,"APP/homepage.html", {'books':books})

def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        pass
    return render(request,'app/create_book.html',{'form':form})