from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Author(models.Model):
      
    name = models.CharField(max_length=100)
    dob = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50, blank=True, null=True)
    books_in_collection = models.IntegerField(_("Books in Collection"), default=0, blank=True, null=True)

    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs):
    #     books_authored = Book.objects.all().filter(author__name=self.name)
    #     self.books_in_collection = books_authored.count()
    #     super(Author, self).save(*args, **kwargs)


    

