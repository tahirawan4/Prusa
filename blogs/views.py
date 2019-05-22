from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from blogs.models import Post, BlogComment


class PostsList(ListView):
    model = Post
    queryset = Post.objects.filter(is_active=True)
    template_name = 'posts.html'
    context_object_name = 'posts'


class PostDetails(DetailView):
    model = Post
    queryset = Post.objects.filter(is_active=True)
    context_object_name = 'post'
    template_name = 'post_details.html'


class CommentCreate(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ['comment']

    def get_success_url(self):
        return reverse('post-details', kwargs={'slug': self.kwargs.get('slug')})

    def form_valid(self, form):
        post = Post.objects.filter(slug=self.kwargs.get('slug')).first()
        form.instance.post_id = post.id
        form.instance.user = self.request.user
        return super().form_valid(form)
