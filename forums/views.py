from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from blogs.models import Post, BlogComment
from forums.models import ForumCategory, Topic, TopicPosts, TopicAnswer, TopicAnswerComment, TopicVote


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


class TopicAnswerCreate(LoginRequiredMixin, CreateView):
    model = TopicAnswer
    fields = ['content']

    def get_success_url(self):
        return reverse('topic-post-details', kwargs={'slug': self.kwargs.get('slug')})

    def form_valid(self, form):
        post = TopicPosts.objects.filter(slug=self.kwargs.get('slug')).first()
        form.instance.topic_post_id = post.id
        form.instance.user = self.request.user
        return super().form_valid(form)


class TopicAnswerCommentCreate(LoginRequiredMixin, CreateView):
    model = TopicAnswerComment
    fields = ['content']

    def get_success_url(self):
        return reverse('topic-post-details', kwargs={'slug': self.kwargs.get('slug')})

    def form_valid(self, form):
        post = TopicAnswer.objects.filter(id=self.kwargs.get('id')).first()
        form.instance.topic_answer_id = post.id
        form.instance.user = self.request.user
        return super().form_valid(form)


# class UpVoteView(LoginRequiredMixin, TemplateView):
#     model = TopicAnswerComment
#     fields = ['content']
#
#     def get_success_url(self):
#         return reverse('topic-post-details', kwargs={'slug': self.kwargs.get('slug')})
#
#     def form_valid(self, form):
#         post = TopicAnswer.objects.filter(id=self.kwargs.get('id')).first()
#         form.instance.topic_answer_id = post.id
#         form.instance.user = self.request.user
#         return super().form_valid(form)

@login_required
def up_vote(request, slug, answer_id):
    topic_answer = TopicAnswer.objects.filter(id=answer_id).first()
    topic_vote, _ = TopicVote.objects.get_or_create(topic_answer=topic_answer, vote=1, user=request.user)
    topic_vote.vote = 1
    topic_vote.save()
    return redirect(reverse('topic-post-details', kwargs={'slug': slug}))


@login_required
def down_vote(request, slug, answer_id):
    topic_answer = TopicAnswer.objects.filter(id=answer_id).first()
    topic_vote, _ = TopicVote.objects.get_or_create(topic_answer=topic_answer, vote=1, user=request.user)
    topic_vote.vote = -1
    topic_vote.save()
    return redirect(reverse('topic-post-details', kwargs={'slug': slug}))
