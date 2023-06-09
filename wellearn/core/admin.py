from django.contrib import admin
from .models import (HomePage, Courses, About, BelowBanner,
                     AboutPoint, CoursesPoint, Resources,
                     ResourcesPoint, GetInTouch,
                     Settings, HowItWorks, HowItWorksPoint,
                     NewsLetters)
# Register your models here.
admin.site.register(HomePage)
admin.site.register(BelowBanner)
admin.site.register(Settings)
admin.site.register(NewsLetters)
admin.site.register(GetInTouch)

class PointInlineAdim(admin.StackedInline):
    model = HowItWorksPoint
    extra = 1
@admin.register(HowItWorks)
class HowItWorksAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [PointInlineAdim] 


class PointInlineAdim(admin.StackedInline):
    model = ResourcesPoint
    extra = 1
@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [PointInlineAdim] 
  

class PointInlineAdim(admin.StackedInline):
    model = CoursesPoint
    extra = 1
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [PointInlineAdim] 
  

class PointIlineAdim(admin.StackedInline):
    model = AboutPoint
    extra = 1
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [PointIlineAdim]
    
    


    
# @admin.register(BlogAuthor)
# class BlogAuthorAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'age', 'blog_count']

#     def blog_count(self, obj):
#         return obj.auth_posts.count()
    
#     blog_count.short_description = 'Blog Count'

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ['title', 'published_at', 'slug', 'get_author_first_name']
#     prepopulated_fields = {'slug': ('title',)} 

#     def get_author_first_name(self, obj):
#         return obj.blog_author.first_name

#     get_author_first_name.short_description = 'Author First Name'