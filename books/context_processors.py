from .models import Book

def total_books(request):
    all_books = Book.objects.all()
    counter = all_books.count()
    return {'counter': counter}
    