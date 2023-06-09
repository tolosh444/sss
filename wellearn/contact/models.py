from django.db import models
from django.utils.translation import gettext_lazy as _

class ContactUs(models.Model):
    full_name = models.CharField(
        _('Full_name'),
        max_length=50
    )
    email = models.EmailField(
        _('Email'),
        max_length=100
    )
    message = models.TextField(
        _('Text')
    )
    phone_number = models.CharField(
        _('Phone Num'),
        max_length=13,
        null=True,
        blank=True
        
    )
    
    
    created_at = models.DateTimeField(
        _('Created_at'),
        auto_now_add=True,
    )
    class Meta:
        verbose_name = _('Contact us')
        verbose_name_plural = _('Contacts us')

