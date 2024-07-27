from django.shortcuts import render

# Import HttpResponse to send text-based responses for testing
from django.http import HttpResponse


class Author:
    def __init__(self, name, date_of_birth, nationality):
        self.name = name
        self.date_of_birth = date_of_birth
        self.nationality = nationality


authors = [
    Author("William Shakespeare", "April 23, 1564", "English"),
    Author("Jane Austen", "December 16, 1775", "English"),
    Author("J.K. Rowling", "July 31, 1965", "British"),
    Author("George Orwell", "June 25, 1903", "British"),
]


# Create your views here.
def home(request):
    return render(request, "home.html")


def author_index(request):
    return render(request, 'authors/index.html', {'authors': authors})


def detail(request):
    return HttpResponse("Detail Page")
