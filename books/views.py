from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Review
from django.views import View
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

class ListingView(View):
    form_class = ReviewForm
    class_template = 'books/listing.html'

    def get(self, request, id):
        form = self.form_class()
        book = get_object_or_404(Book, pk=id)
        comments = Review.objects.all().filter(book=book)
        context = {
            'book': book,
            'form': form,
            'comments': comments,
        }
        return render(request, self.class_template, context)

    def post(self, request, id):
        book = get_object_or_404(Book, pk=id)
        
        form = self.form_class(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.username = request.user.username
            post.book = book
            post.save()
            return redirect('class_list', id=id)
        
        
        # return render(request,  self.class_template, {'book': book, 'form':form})