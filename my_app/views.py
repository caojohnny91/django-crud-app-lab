from django.shortcuts import render

# Import HttpResponse to send text-based responses for testing
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "home.html")


def index(request):
    return HttpResponse("<h1>Index BookCollector</h1>")


def detail(request):
    return HttpResponse("Detail Page")
