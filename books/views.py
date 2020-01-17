from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Review
from django.views import View
from .forms import ReviewForm
from django.db.models import Q
from django.views.generic import View
from django.core.serializers import serialize
# import json
from django.http import JsonResponse, HttpResponse 

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

def book_api(request):
    context = {
        'name': 'Head first Java',
        'author': 'Kathy Bates'
    }
    # data = json.dumps(context)
    # return HttpResponse(data, content_type='application/json')
    return JsonResponse(context)

class BookAPI(View):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        data = serialize('json', books, fields=('name', 'author', 'published_on', 'genre'))
        # context = {
        #     'name': 'Head first Java',
        #     'author': 'Kathy Bates'
        # }
        return HttpResponse(data, content_type='application/json')
