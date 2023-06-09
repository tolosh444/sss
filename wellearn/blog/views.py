from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.urls import reverse_lazy
from core.models import About, Courses, Resources
from blog.utils import DataMixin 
from .models import Blog, Category
from django.views import View, generic
from .forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import DeleteView

# Create your views here.

# def blogs(request):
   
#     courses = Courses.objects.first()
#     about = About.objects.first()
#     resources = Resources.objects.first()
#     blogs = Blog.objects.all()
#     last_blogs = Blog.objects.all().order_by('-published_at')
#     category = Category.objects.all()
#     context={
#         'about': about,
#         'courses' : courses,
#         'resources' : resources,
#         'blogs' : blogs,
#         'last_blogs': last_blogs,
#         'category' : category
        

#     }
#     return render(request, 'blog/blogs.html', context)

def blog_details(request, slug):
    courses = Courses.objects.first()
    about = About.objects.first()
    resources = Resources.objects.first()
    first_blog = Blog.objects.first()
    blog = Blog.objects.get(slug=slug)
    last_blogs = Blog.objects.all().order_by('-published_at')[:3]
    category = Category.objects.all()
    
    context={
        'about': about,
        'courses' : courses,
        'resources' : resources,
        'first_blog': first_blog, # E
        'blog' : blog,
        'last_blogs': last_blogs,
        'category' : category

    }
    return render(request, 'blog/blog-details.html', context)
    
class CreateBlogView(LoginRequiredMixin, generic.CreateView):
    form_class = BlogForm
    template_name = 'blog/create.html'
    model = Blog
    success_url = reverse_lazy('blogs')
    
    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.blog_author = self.request.user
        blog.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    

class MyBlogsView(View):
    def get(self, request):
        my_blogs = Blog.objects.filter(blog_author=self.request.user).order_by('-published_at')[:3]
        return render(request, 'blog/my-blogs.html', {'my_blogs': my_blogs})
    
    
    
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url=reverse_lazy("blogs")
    template_name = "blog/blog-details.html"
    # slug_url_kwarg = 'blog_slug' bunu eger slugin adini deyishiremse 
    
    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.blog_author:
            return True
        return False
    
class BlogUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Blog
    success_url=reverse_lazy("blogs")
    template_name = "blog/create.html"
    form_class = BlogForm
    
class BlogListView(ListView):
    paginate_by = 3
    model = Blog
    template_name = "blog/blogs.html"
    


# def blog_listing(request):
    
#     courses = Courses.objects.first()
#     about = About.objects.first()
#     resources = Resources.objects.first()
#     blogs = Blog.objects.all()
#     last_blogs = Blog.objects.all().order_by('-published_at')
#     category = Category.objects.all()

    
#     blog_list = Blog.objects.all().order_by('-published_at')
#     paginator = Paginator(blog_list, 3)

#     page_number = request.GET.get("page")
#     current_page = paginator.get_page(page_number)
    
#     try:
#         next_page_number = current_page.next_page_number()
#         next_next_page_number = next_page_number + 1
#     except EmptyPage:
#         next_page_number = None
#         next_next_page_number = None
        
#     page_obj = paginator.get_page(page_number)
    
#     context = {
#         "page_obj": page_obj, 
#         "next_next_page_number": next_next_page_number,
        
#         'about': about,
#         'courses' : courses,
#         'resources' : resources,
#         'blogs' : blogs,
#         'last_blogs': last_blogs,
#         'category' : category
        
        
#     }
#     return render(request, "blog/blogs.html", context)