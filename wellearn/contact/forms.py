from django import forms
from .models import ContactUs
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Name Surname'),
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': _('Email'),
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': _('Text'),
        'rows': '4',
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Phone number'),
    }))
    

    
    class Meta:
        model = ContactUs
        fields = ['full_name','email' ,'message' ,'phone_number']
        
        
