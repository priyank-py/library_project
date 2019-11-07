from django.db import models
from datetime import date

# Create your models here.
class Book(models.Model):

    GENRE_CHOICES = (
        ('adventure', 'Adventure'), 
        ('history', 'History'), 
        ('fiction', 'Fiction'), 
        ('nonfiction', 'Non-Fiction')
    )

    name = models.CharField(max_length=200, verbose_name='Book Title')
    author = models.CharField(max_length=100)
    pages = models.PositiveSmallIntegerField(blank=True, null=True)
    published_on = models.DateField(default=date.today,blank=True, null=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)

    def __str__(self):
        return self.name
    
    
    
