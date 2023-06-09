from .models import *
from core.models import *
from contact.models import *
from account.models import *




class DataMixin:
    def get_categories(self):
        return Category.objects.filter(category_post=self.object)

    def get_author(self):
        return self.object.blog_author

    def get_image_url(self):
        return self.object.blog_image.url

    def get_user_context(self, **kwargs):
        user = self.request.user
        # Additional context data for the user
        user_context = {
            'user': user,
            # Add more context data as needed
        }
        if kwargs:
            user_context.update(kwargs)
        return user_context

