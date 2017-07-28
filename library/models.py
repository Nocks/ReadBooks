from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ManyToManyField(Author, help_text="Select the author(s) for this book.")
    year = models.CharField(max_length=4)
    isbn = models.CharField(max_length=13, help_text='13 or 10 Character. <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    publisher = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='uploads/book_covers/%Y/%m/')
    genre = models.ManyToManyField('Genre', help_text="Select the genre(s) of this book.")
    BOOK_STATUS = (
        ('UNREAD', 'Unread'),
        ('TOREAD', 'To read'),
        ('READING', 'Reading'),
        ('READ', 'Read'),
    )
    status = models.CharField(max_length=7,
                              choices=BOOK_STATUS,
                              default='UNREAD'
                              )
    date_added = models.DateField(auto_now_add=True, auto_now=False)
    last_modified = models.DateField(auto_now=True, auto_now_add=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = (("title", "owner"),)


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField(max_length=800)
    BOOK_RATING = (
        ('NOT_RATED', 'Not Rated'),
        ('ONE', 1),
        ('TWO', 2),
        ('THREE', 3),
        ('FOUR', 4),
        ('FIVE', 5),
    )
    rating = models.CharField(max_length=9,
                              choices=BOOK_RATING,
                              default='NOT_RATED')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True, auto_now=False)
    last_modified = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.review[:30]
