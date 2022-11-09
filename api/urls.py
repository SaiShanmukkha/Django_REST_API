from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.blogpost_list_view, name="index"),
    path(route='posts', view=views.blogpost_list_view, name="posts"),
    path(route='posts/<slug:slug>', view=views.blogpost_retrieve_view, name="posts-slug")
]


