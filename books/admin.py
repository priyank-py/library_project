from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'author', 'pages', 'published_on']
    list_display_links = ['id', 'name']
    list_filter = ['author', 'genre']
    search_fields = ['id', 'name', 'author',]



