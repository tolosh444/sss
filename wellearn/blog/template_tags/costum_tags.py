import os
import datetime
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def filename(value):
    return os.path.basename(value.file.name)

@register.filter
@stringfilter
def first_upper(value):
    return value.title()
 
 
@register.simple_tag(name="minustwo")
def some_function(value):
    return value - 1