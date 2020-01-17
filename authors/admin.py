from django.contrib import admin
from .models import Author
from .forms import AuthorForm
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'language']
    form = AuthorForm

admin.site.register(Author, AuthorAdmin)
