from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from api.serializers import BlogPostSerializer
from api.models import BlogPost

# Create your views here.

@api_view(["GET"])
def greet(request, *args, **kwargs):
    dt = timezone.localtime(timezone.now())
    return Response({"Message": "Hello", "DateTime":dt})


class BlogPostsList(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # lookup_field = BlogPost.slug

    

    

blogpost_list_view = BlogPostsList.as_view()