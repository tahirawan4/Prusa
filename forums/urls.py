# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from forums import views

urlpatterns = [
    path('', views.ForumList.as_view(), name='forums'),
    path('<slug:slug>/details/', views.ForumDetails.as_view(), name='forum-details'),
    path('topic/<slug:slug>/details/', views.TopicDetails.as_view(), name='forum-posts'),
    path('post/<slug:slug>/details/', views.PostDetails.as_view(), name='topic-post-details'),
    path('post/<slug:slug>/answer/', views.TopicAnswerCreate.as_view(), name='topic-post-answer'),
    path('post/<slug:slug>/answer/<int:id>/comment/', views.TopicAnswerCommentCreate.as_view(),
         name='topic-post-answer-comment'),
    path('post/<slug:slug>/answer/<int:answer_id>/upvote/', views.up_vote, name='topic-post-answer-upvote'),
    path('post/<slug:slug>/answer/<int:answer_id>/downvote/', views.down_vote, name='topic-post-answer-downvote'),

]
