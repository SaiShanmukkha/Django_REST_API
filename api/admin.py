from django.contrib import admin

from api.models import BlogPost, Tag


# Custom Admin Page Model View

class BlogPostAdminView(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'published_date')
    def get_readonly_fields(self, request, obj=None):
        try:
            return [f.name for f in obj._meta.fields if not f.editable]
        except:
            # if a new object is to be created the try clause will fail due to missing _meta.fields
            return ""


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'foreground', 'background')



# Register your models here.
admin.site.register(BlogPost, BlogPostAdminView)
admin.site.register(Tag, TagAdmin)
