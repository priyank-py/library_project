from django.shortcuts import render
from .models import Author
from books.models import Book
# Create your views here.
def details(request):

    all_authors = Author.objects.all()

    # author_model = 'some'
    # no_books = Book.objects.all().filter(author=author_model)

    books_for_each_author = [Book.objects.all().filter(author=i) for i in all_authors]
    print(len(books_for_each_author[0]))

    context = {
        'all_authors': all_authors,
    }
    
    return render(request, 'author/details.html', context)

