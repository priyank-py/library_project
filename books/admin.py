from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'published_on']
    list_display_links = ['name']
    list_filter = ['genre']
    search_fields = [ 'name', ]



