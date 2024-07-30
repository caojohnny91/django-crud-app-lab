from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView


# Import HttpResponse to send text-based responses for testing
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Author, Book
from .forms import BookForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = ["name", "date_of_birth", "nationality"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ["name", "date_of_birth", "nationality"]


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = "/authors/"


class Home(LoginView):
    template_name = "home.html"


@login_required
def author_index(request):
    authors = Author.objects.filter(user=request.user)
    return render(request, "authors/index.html", {"authors": authors})


@login_required
def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    book_form = BookForm()
    return render(
        request, "authors/detail.html", {"author": author, "book_form": book_form}
    )


@login_required
def add_book(request, author_id):
    form = BookForm(request.POST)
    if form.is_valid():
        new_book = form.save(commit=False)
        new_book.author_id = author_id
        new_book.save()
    return redirect("author-detail", author_id=author_id)


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/update_book.html"

    def get_success_url(self):
        return reverse_lazy(
            "author-detail", kwargs={"author_id": self.object.author.id}
        )


class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "books/delete_book.html"

    def get_success_url(self):
        return reverse_lazy(
            "author-detail", kwargs={"author_id": self.object.author.id}
        )


def signup(request):
    error_message = ""
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect("author-index")
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)
    # Same as:
    # return render(
    #     request,
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )
