from django.shortcuts import render, get_object_or_404 
from .models import Book

# Create your views here.

def home(request):
    all_books = Book.objects.all()
    
    return render(request, 'main/index.html', {'all_books': all_books})

def listings(request):
    all_books = Book.objects.all()
    
    
    context = {
        'all_books': all_books,
    }
    return render(request, 'books/listings.html', context)


def listing(request, id):
    book = get_object_or_404(Book, pk=id)


    return render(request, 'books/listing.html', {'book': book})