from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    # add routes below
    path("", views.home, name="home"),
    path("authors/", views.author_index, name="author-index"),
    path("detail/", views.detail, name="detail"),
]
