import uuid
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class UUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True

class BlogPost(UUIDModel):
    title = models.CharField(max_length=200, help_text="Enter Blog Post Title", null=False, verbose_name="Title")
    slug = models.SlugField(max_length=100, help_text="Enter Blog Post Slug", unique=True)
    published_date = models.DateTimeField(help_text="Blog Post Published Date", verbose_name="Published Date", editable=False, null=True)
    Last_modified_date = models.DateTimeField(help_text="Blog post Last Modified Date", verbose_name="Last Modified Date", editable=False, null=True)
    content_url = models.TextField(help_text='Enter Blog Post Content', verbose_name="Blog Post Body")
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the Blog Post')
    image = models.ImageField(upload_to="api/static/images/", default="api/static/images/todo.png")

    def post_absolute_url(self):
        return reverse('posts-slug', kwargs={'slug':self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.pkid:
            self.published_date = timezone.localtime(timezone.now())
        self.Last_modified_date = timezone.localtime(timezone.now())
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Tag(models.Model):
    name=models.CharField(max_length=30, help_text="Enter Tag Name", null=False, verbose_name="Tag")
    foreground=models.CharField(max_length=100, help_text="Enter Foreground Decoration",verbose_name="Foreground", default="#fff")
    background=models.CharField(max_length=100, help_text="Enter Background Decoration",verbose_name="Background", default="#000")
     

