from django.urls import path
from . import views  # Import views to connect routes to view functions

urlpatterns = [
    # add routes below
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("detail/", views.detail, name="detail"),
]
