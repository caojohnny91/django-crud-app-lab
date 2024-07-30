from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    # add routes below
    path("", views.Home.as_view(), name="home"),
    path("authors/", views.author_index, name="author-index"),
    path("authors/<int:author_id>", views.author_detail, name="author-detail"),
    path("authors/create/", views.AuthorCreate.as_view(), name="author-create"),
    path("<int:pk>/update", views.AuthorUpdate.as_view(), name="author-update"),
    path("<int:pk>/delete", views.AuthorDelete.as_view(), name="author-delete"),
    path("cats/<int:author_id>/add-book/", views.add_book, name="add-book"),
    path(
        "authors/<int:author_id>/update-book/<int:pk>/",
        views.BookUpdate.as_view(),
        name="update-book",
    ),
    path(
        "authors/<int:author_id>/delete-book/<int:pk>/",
        views.BookDelete.as_view(),
        name="delete-book",
    ),
    path('accounts/signup/', views.signup, name='signup'),

]
