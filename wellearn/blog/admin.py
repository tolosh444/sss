from django.contrib import admin

from blog.models import Blog, Category

# # Register your models here.
# @admin.register(BlogAuthor)
# class BlogAuthorAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'age', 'blog_count']

#     def blog_count(self, obj):
#         return obj.auth_posts.count()
    
#     blog_count.short_description = 'Blog Count'

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'slug', 'get_author_first_name', 'get_category_name']
    prepopulated_fields = {'slug': ('title',)} 

    def get_author_first_name(self, obj):
        return obj.blog_author.first_name

    get_author_first_name.short_description = 'Author First Name'
    
    def get_category_name(self, obj):
        return ', '.join(category.name for category in obj.category.all())

    get_category_name.short_description = 'Category Name'
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)} 