from django.shortcuts import render
from django.views import View
from library.models import Author, Book, Genre, Review


def index(request):
    all_books = Book.objects.all()

    return render(
        request,
        'library/index.html',
        context={"all_books": all_books}
    )
