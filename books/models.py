from django.db import models
from datetime import date
from django.shortcuts import reverse
from authors.models import Author
from django.utils.translation import ugettext_lazy as _


def upload_book(instance, filename):
    return f'{instance.author.name}/{filename}'

class Book(models.Model):

    GENRE_CHOICES = (
        ('adventure', 'Adventure'), 
        ('history', 'History'), 
        ('fiction', 'Fiction'), 
        ('nonfiction', 'Non-Fiction')
    )

    name = models.CharField(max_length=200, verbose_name='Book Title')
    author = models.ForeignKey(Author,on_delete=models.CASCADE, null=True, blank=True)
    book_src = models.FileField(_("Book Source"), upload_to=upload_book, blank=True, null=True)
    pages = models.PositiveSmallIntegerField(blank=True, null=True)
    published_on = models.DateField(default=date.today,blank=True, null=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    photo = models.ImageField(upload_to='Book_Covers/', height_field=None, width_field=None, max_length=1000, blank=True, null=True)
    summary = models.TextField(_("Summary"), blank=True, null=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("listing", kwargs={"id": self.pk})
    
    
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
    
    
class Review(models.Model):

    STAR_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    book = models.ForeignKey(Book, verbose_name=_("Book"), related_name='book_review', on_delete=models.CASCADE)
    username = models.CharField(_("Username"), max_length=50)
    stars = models.IntegerField(_("Stars"), choices=STAR_CHOICES)
    comment = models.TextField(_("Your Comment"), blank=True, null=True)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("Review_detail", kwargs={"pk": self.pk})
