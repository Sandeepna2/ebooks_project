from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BookAuthor(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='author')
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='authors/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class BookCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE , related_name='books')
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name='books')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)
    published_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.title} by {self.author}'
