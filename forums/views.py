from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from blogs.models import Post, BlogComment
from forums.models import ForumCategory, Topic, TopicPosts


class ForumList(ListView):
    model = ForumCategory
    queryset = ForumCategory.objects.filter(is_active=True)
    context_object_name = 'forum_categories'
    template_name = 'forums.html'


class ForumDetails(DetailView):
    model = ForumCategory
    template_name = 'all_topics.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['topics'] = Topic.objects.filter(category__slug=self.kwargs.get('slug'))
        return super().get_context_data(**context)


class TopicDetails(DetailView):
    model = Topic
    template_name = 'all_posts.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['posts'] = TopicPosts.objects.filter(topic__slug=self.kwargs.get('slug'))
        return super().get_context_data(**context)


class PostDetails(DetailView):
    model = TopicPosts
    template_name = 'forum_post_details.html'
    context_object_name = 'post'
