from django.urls import path
from . import views

urlpatterns = [
    path(route='hello', view=views.hello, name='hello',)
]

