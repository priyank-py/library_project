from django.db import models

# Create your models here.

class Author(models.Model):
      
    name = models.CharField(max_length=100)
    dob = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.name

    

