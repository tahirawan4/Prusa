from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ForumCategory(BaseModel):
    title = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title


class Topic(BaseModel):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title')

    @property
    def get_last_post(self):
        return self.topicposts_set.all().order_by('-id').first()

    def __str__(self):
        return self.title


class TopicPosts(BaseModel):
    title = models.CharField(max_length=500)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    slug = AutoSlugField(populate_from='title', default='test-slug')

    def __str__(self):
        return self.title


class TopicAnswer(BaseModel):
    topic_post = models.ForeignKey(TopicPosts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()


class TopicVote(BaseModel):
    topic_answer = models.ForeignKey(TopicAnswer, on_delete=models.CASCADE)
    vote = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
