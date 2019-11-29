from django.db import models
from datetime import date
from authors.models import Author
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Book(models.Model):

    GENRE_CHOICES = (
        ('adventure', 'Adventure'), 
        ('history', 'History'), 
        ('fiction', 'Fiction'), 
        ('nonfiction', 'Non-Fiction')
    )

    name = models.CharField(max_length=200, verbose_name='Book Title')
    author = models.ForeignKey(Author,on_delete=models.CASCADE, null=True, blank=True)
    pages = models.PositiveSmallIntegerField(blank=True, null=True)
    published_on = models.DateField(default=date.today,blank=True, null=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    photo = models.ImageField(upload_to='Book_Covers/', height_field=None, width_field=None, max_length=1000, blank=True, null=True)
    summary = models.TextField(_("Summary"), blank=True, null=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # if self.author.books_in_collection:
        #     self.author.books_in_collection += 1
        # else:
        #     self.author.books_in_collection = 1
        # print(self.author.books_in_collection)
        if len(self.summary) == 0:
            self.summary = f'''
The {self.genre} themed book {self.name} written by {self.author} was published on {self.published_on}.
            '''
        super(Book, self).save(*args, **kwargs)
    
    
