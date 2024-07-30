from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView


# Import HttpResponse to send text-based responses for testing
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Author, Book
from .forms import BookForm
from django.urls import reverse_lazy

# Create your views here.


class AuthorCreate(CreateView):
    model = Author
    fields = ["name", "date_of_birth", "nationality"]
    success_url = "/authors/"


class AuthorUpdate(UpdateView):
    model = Author
    fields = ["name", "date_of_birth", "nationality"]


class AuthorDelete(DeleteView):
    model = Author
    success_url = "/authors/"


class Home(LoginView):
    template_name = "home.html"


def author_index(request):
    authors = Author.objects.all()
    return render(request, "authors/index.html", {"authors": authors})


def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    book_form = BookForm()
    return render(
        request, "authors/detail.html", {"author": author, "book_form": book_form}
    )


def add_book(request, author_id):
    form = BookForm(request.POST)
    if form.is_valid():
        new_book = form.save(commit=False)
        new_book.author_id = author_id
        new_book.save()
    return redirect("author-detail", author_id=author_id)


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/update_book.html"

    def get_success_url(self):
        return reverse_lazy(
            "author-detail", kwargs={"author_id": self.object.author.id}
        )


class BookDelete(DeleteView):
    model = Book
    template_name = "books/delete_book.html"

    def get_success_url(self):
        return reverse_lazy(
            "author-detail", kwargs={"author_id": self.object.author.id}
        )
