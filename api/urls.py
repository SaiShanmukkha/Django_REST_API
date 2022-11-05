from django.urls import path
from . import views

urlpatterns = [
    path(route='hello', view=views.greet, name='greet',),
    path(route='blogposts/<slug:slug>', view=views.blogpost_list_view, name="posts")
]

