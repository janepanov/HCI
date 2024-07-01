from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Book(models.Model):
    BOOK_GENRES = [
        ("Romance", "Romance"),
        ("Thriller", "Thriller"),
        ("Science Fiction", "Science Fiction"),
        ("Fantasy", "Fantasy"),
        ("Historical Fiction", "Historical Fiction"),
    ]
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, choices=BOOK_GENRES)
    isbn = models.CharField(max_length=30)
    is_read = models.BooleanField(default=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    publish_date = models.DateField()
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.genre}"


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    biography = models.TextField(max_length=200)
    birth_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Member(models.Model):
    full_name = models.CharField(max_length=100)
    join_date = models.DateField()

    def __str__(self):
        return self.full_name


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} - {self.author}"
