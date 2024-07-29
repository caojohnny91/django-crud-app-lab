from django.shortcuts import render

# Import HttpResponse to send text-based responses for testing
from django.http import HttpResponse
from .models import Author


# Create your views here.
def home(request):
    return render(request, "home.html")


def author_index(request):
    authors = Author.objects.all()
    return render(request, "authors/index.html", {"authors": authors})


def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, "authors/detail.html", {"author": author})
