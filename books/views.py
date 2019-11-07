from django.shortcuts import render
from .models import Book

# Create your views here.

def home(request):
    all_books = Book.objects.all()
    print(all_books)
    return render(request, 'main/index.html', {'all_books': all_books})