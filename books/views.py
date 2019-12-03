from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import ReviewForm
from django.db.models import Q

# Create your views here.

def home(request):
    all_books = Book.objects.all()
    
    return render(request, 'main/index.html', {'all_books': all_books})

def listings(request):
    query = request.GET.get('q')
    if not query == None:
        all_books = Book.objects.all().filter(
            Q(name__icontains=query) | 
            Q(author__name__icontains=query)
        )
    else:
        all_books = Book.objects.all()
    
    
    context = {
        'all_books': all_books,
    }
    return render(request, 'books/listings.html', context)


def listing(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.username = request.user.username
            post.book = book
            post.save()
        return redirect('listing', id=id)
    else:
        form = ReviewForm()
    return render(request, 'books/listing.html', {'book': book, 'form':form})