from django import forms
from .models import Blog, Category


class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
         'rows': '6',
     }))

    
    
    class Meta:
        model = Blog
        fields = ['title', 'content', 'blog_image', 'published_at', 'category']