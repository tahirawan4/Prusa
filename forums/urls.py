# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from forums import views

urlpatterns = [
    path('', views.ForumList.as_view(), name='forums'),
    path('<slug:slug>/details/', views.ForumDetails.as_view(), name='forum-details'),
    path('topic/<slug:slug>/details/', views.TopicDetails.as_view(), name='forum-posts'),
    path('post/<slug:slug>/details/', views.PostDetails.as_view(), name='post-details'),
    # path('<slug:slug>/comment/', views.CommentCreate.as_view(), name='post-comment'),
]
