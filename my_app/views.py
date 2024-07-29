from django.shortcuts import render

# Import HttpResponse to send text-based responses for testing
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Author

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


def home(request):
    return render(request, "home.html")


def author_index(request):
    authors = Author.objects.all()
    return render(request, "authors/index.html", {"authors": authors})


def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, "authors/detail.html", {"author": author})
