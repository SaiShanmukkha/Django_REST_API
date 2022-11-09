from rest_framework import serializers
from .models import BlogPost
from django.urls import reverse

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "title",
            "slug",
            "published_date",
        ]
        read_only_fields = [
            "title",
            "slug",
            "published_date",
        ]

    
class BlogPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "published_date",
            "content_url",
            "summary",
        ]
        read_only_fields =["slug"]



