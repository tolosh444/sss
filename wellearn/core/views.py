from django.shortcuts import render
from django.views import View
from core.models import (
    HomePage, BelowBanner, 
    About, Courses, Resources,
    GetInTouch, HowItWorks,
    NewsLetters, )
from blog.models import (
    Blog)
# # Create your views here.



def index(request):
    banner = HomePage.objects.first()
    below_banners = BelowBanner.objects.all()
    courses = Courses.objects.first()
    about = About.objects.first()
    resources = Resources.objects.first()
    getintouch = GetInTouch.objects.first()
    howitworks = HowItWorks.objects.first()
    newsletters = NewsLetters.objects.first()
    # bl_author = BlogAuthor.objects.first()
    blogs = Blog.objects.all()
    
    
    context={
        'banner': banner,
        'below_banners': below_banners,
        'about': about,
        'courses' : courses,
        'resources' : resources,
        'getintouch': getintouch,
        'howitworks': howitworks,
        'newsletters' : newsletters,
        # 'author': bl_author,
        'blogs' : blogs
        
    }
    return render(request,'home/index.html', context)



def about(request):
    banner = HomePage.objects.first()
    below_banners = BelowBanner.objects.all()
    courses = Courses.objects.first()
    about = About.objects.first()
    resources = Resources.objects.first()
    getintouch = GetInTouch.objects.first()
    howitworks = HowItWorks.objects.first()
    newsletters = NewsLetters.objects.first()
    blogs = Blog.objects.all()
    
    context={
        'banner': banner,
        'below_banners': below_banners,
        'about': about,
        'courses' : courses,
        'resources' : resources,
        'getintouch': getintouch,
        'howitworks': howitworks,
        'newsletters' : newsletters,
        # 'author': bl_author,
        'blogs' : blogs

    }
    return render(request, 'about/about.html', context)


