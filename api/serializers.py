from rest_framework import serializers
from .models import BlogPost
from django.urls import reverse

class BlogPostSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    def get_absolute_url(self, obj):
        return 'http://localhost:8000/'+obj.post_absolute_url()

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "slug",
            "published_date",
            "absolute_url",
            "image"
        ]
        read_only_fields = [
            "id",
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
            "image"
        ]
        read_only_fields =["slug"]

class BlogPostSlugs(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "slug"
        ]

