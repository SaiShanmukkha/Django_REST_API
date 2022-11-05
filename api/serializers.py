from rest_framework import serializers
from .models import BlogPost
from django.urls import reverse

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "published_date",
            "content_url",
            "summary",
            "obsolute_url",
        ]

    



