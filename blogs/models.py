from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogCatrgeory(BaseModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title


class Post(BaseModel):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    categories = models.ManyToManyField(BlogCatrgeory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    main_image = models.ImageField()
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title


class BlogComment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(default='')

    def __str__(self):
        return str(self.id)
