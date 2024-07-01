from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


# Create your views here.

def books(request):
    books = Book.objects.all()
    context = {"books": books}

    return render(request, "books.html", context=context)


def edit_book(request, id):
    book_instance = Book.objects.filter(id=id).first()
    form = BookForm(instance=book_instance)

    if request.method == "POST":
        form = BookForm(request.POST, files = request.FILES, instance=book_instance)

        if form.is_valid():
            book = form.save(commit=False)
            book.cover_image = form.cleaned_data['cover_image']
            book.save()
        return redirect('books')

    return render(request, "edit_book.html", {"form": form})

