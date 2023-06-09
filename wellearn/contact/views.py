from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from core.models import About, Courses, Resources
from .forms import ContactForm 

# Create your views here.

def contact(request):
    courses = Courses.objects.first()
    about = About.objects.first()
    resources = Resources.objects.first()

    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Thank you for contacting us! We will be in touch shortly."))
            return redirect(reverse_lazy("contact"))
        else:
            messages.error(request, ("Something went wrong!!!"))
            return redirect(reverse_lazy("contact"))
    context = {
        'form': form,
        'resources': resources,
        'courses': courses,
        'about': about,
        
    }
    return render(request, 'contact/contact.html', context)




