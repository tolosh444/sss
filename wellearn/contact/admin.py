from django.contrib import admin
from .models import ContactUs

# Register your models here.

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'created_at']
    

