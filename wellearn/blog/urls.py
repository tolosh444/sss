from django.contrib import admin
from django.urls import path
from .views import  BlogListView, blog_details , CreateBlogView , MyBlogsView, BlogDeleteView, BlogUpdateView

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('my-blogs/', MyBlogsView.as_view(), name='my_blogs'),
    path('blog-details/<slug:slug>/', blog_details, name='blog_details'),    
    path('blogs/create', CreateBlogView.as_view(), name='blog_create'),
    path('blog-details/<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog-details/<slug:slug>/update/', BlogUpdateView.as_view(), name='blog_update')
]