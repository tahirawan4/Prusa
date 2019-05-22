# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView  # new
from blogs import views

urlpatterns = [
    path('', views.PostsList.as_view(), name='posts'),
    path('<slug:slug>/details/', views.PostDetails.as_view(), name='blog-post-details'),
    path('<slug:slug>/comment/', views.CommentCreate.as_view(), name='post-comment'),
]
