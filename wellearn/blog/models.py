from typing import Iterable, Optional
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(_("Title"), max_length=70)
    content = models.TextField(_("Content"), blank=True)
    published_at = models.DateTimeField(_("Published_at"), auto_now_add=True)
    blog_image = models.ImageField(_("Image"), upload_to="BlogIMG")
    slug = models.SlugField(unique=True)
    blog_author = models.ForeignKey(
        'account.Account',
        on_delete=models.CASCADE,
        null=True,
        related_name="auth_posts"
    )
    category = models.ManyToManyField(
        'blog.Category', 
        related_name='category_post'
        
    )


    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ["-published_at"]

    def __str__(self):
        return self.title
    
    
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(_('Name'),max_length=50)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
