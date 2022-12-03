from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_http_methods

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from api.serializers import BlogPostSerializer,BlogPostDetailSerializer, BlogPostSlugs
from api.models import BlogPost

# Create your views here.

class BlogPostsList(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

blogpost_list_view = BlogPostsList.as_view()
    
class BlogPostRetreive(generics.RetrieveUpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostDetailSerializer
    lookup_field = BlogPost.slug
    
    def get_object(self):
        obj = get_object_or_404(self.queryset, slug=self.kwargs['slug'])
        return obj    

blogpost_retrieve_view = BlogPostRetreive.as_view()


class BlogPostSlugs(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSlugs

blogpost_slugs_retrive_view = BlogPostSlugs.as_view()
