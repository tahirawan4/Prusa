from django.contrib import admin
from blogs.models import BlogCatrgeory, Post, BlogComment

admin.site.register(BlogCatrgeory)
admin.site.register(Post)
admin.site.register(BlogComment)
