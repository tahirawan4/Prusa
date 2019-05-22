from django.contrib import admin
from forums.models import ForumCategory, Topic, TopicPosts, TopicAnswer, Tag

admin.site.register(ForumCategory)
admin.site.register(Topic)
admin.site.register(TopicPosts)
admin.site.register(TopicAnswer)
admin.site.register(Tag)
