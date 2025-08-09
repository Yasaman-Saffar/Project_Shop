from django.db import models
from django.utils.text import slugify


class tickets(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    title = models.CharField(max_length=255)
    content = models.CharField()

class Products(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)
    image = models.ImageField(upload_to='products/')
    description = models.CharField(max_length=500)
    information = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    
    
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name) 
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name