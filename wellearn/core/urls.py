from django.contrib import admin
from django.urls import path
from .views import index, about

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    # path('blogs/', blogs, name='blogs'),
    # path('blog-details/<slug:slug>/', blog_details, name='blog_details'),# ishlemir
]