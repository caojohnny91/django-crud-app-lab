from django.shortcuts import render
# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>BookCollector Home Page</h1>')

def index(request):
    return HttpResponse('<h1>Index BookCollector</h1>')

def detail(request):
    return HttpResponse('Detail Page')