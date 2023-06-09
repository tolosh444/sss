from django.db import migrations , models
from django.utils.translation import gettext_lazy as _
import uuid

class HomePage(models.Model):
    lil_title = models.CharField(_("lTitle"), max_length=250, blank=True)
    title = models.CharField(_("Title"), max_length=250)
    content = models.TextField(_('Content'), blank=True)
    link_content = models.TextField(_('lContent'), blank=True)
    
    class Meta:
        verbose_name = 'HomePage'
        verbose_name_plural = 'HomePage'   
        
    def __str__(self):
        return self.title
    
class BelowBanner(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    content = models.TextField(_('Content'), blank=True)
    image = models.ImageField(_('Image'),upload_to='Below_Banner')
    
    class Meta:
        verbose_name = 'BelowBanner'
        verbose_name_plural = 'BelowBanner'   
        
    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    content = models.TextField(_('Content'), blank=True)
    image = models.ImageField(
        _('Image'),
        upload_to='About',
        default='default_image.png')
 
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'   
        
    def __str__(self):
        return self.title
    
    
class AboutPoint(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    content = models.TextField(_('Content'), blank=True)
    
    workingh = models.ForeignKey(
        About, on_delete=models.CASCADE,
        null=True,
        related_name='points')
    
    class Meta:
        verbose_name = 'AboutPoint'
        verbose_name_plural = 'AboutPoints'   
        
    def __str__(self):
        return self.title
    
class Courses(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    class Meta:
        verbose_name = 'Courses'
        verbose_name_plural = 'Courses'   
        
        def __str__(self):
            return self.title
        
class CoursesPoint(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    url = models.CharField(_("Url"), max_length=50, default='about')
    courses = models.ForeignKey(
        Courses, on_delete=models.CASCADE,
        null=True,
        related_name='cou_points')
    
    class Meta:
        verbose_name = 'CoursesPoint'
        verbose_name_plural = 'CoursesPoint'   
        
    def __str__(self):
        return self.title        
        
class Resources(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    class Meta:
        verbose_name = 'Resources'
        verbose_name_plural = 'Resources'   
        
        def __str__(self):
            return self.title
        
class ResourcesPoint(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    url = models.CharField(_("Url"), max_length=50, default='/')
    resources = models.ForeignKey(
        Resources, on_delete=models.CASCADE,
        null=True,
        related_name='res_points')
    
    class Meta:
        verbose_name = 'ResourcesPoint'
        verbose_name_plural = 'ResourcesPoint'   
        
    def __str__(self):
        return self.title   
    
class GetInTouch(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    class Meta:
        verbose_name = 'GetInTouch'
        verbose_name_plural = 'GetInTouch'   
        
        def __str__(self):
            return self.title
        

class Settings(models.Model):
    title = models.CharField(_("Title"),max_length=100, default='Title')
    logo = models.ImageField(_("Logo"),upload_to='Settings')
    adress = models.CharField(_("Adress"),max_length=100)
    phone = models.CharField(_("Phone"),max_length=15, null=True)
    email = models.EmailField(_("Email"))
    worktime = models.CharField(_("Worktime"),max_length=50,default='')
    year= models.CharField(_("Year"),max_length=10, default='')
    facebook = models.URLField()
    youtube = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    twitter = models.URLField()
    pinterest = models.URLField()
    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'   
        
    def __str__(self):
        return self.title
    
class HowItWorks(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    content = models.TextField(_('Content'), blank=True)
    class Meta:
        verbose_name = 'HowItWorks'
        verbose_name_plural = 'HowItWorks'   
        
        def __str__(self):
            return self.title
        
class HowItWorksPoint(models.Model):
    number = models.IntegerField()
    title = models.CharField(_("Title"), max_length=250)
    content = models.TextField(_('Content'), blank=True)
    howitworks = models.ForeignKey(
        HowItWorks, on_delete=models.CASCADE,
        null=True,
        related_name='hiw_points')
    
    class Meta:
        verbose_name = 'HowItWorksPoint'
        verbose_name_plural = 'HowItWorksPoint'   
        
    def __str__(self):
        return self.title   
    
class NewsLetters(models.Model):
    title = models.CharField(_("Title"), max_length=20)
    content = models.TextField(_('Content'), blank=True)
    description = models.TextField(_('Description'), blank=True)
    button1 = models.CharField(_("Button1"), max_length=15)
    button2 = models.CharField(_("Button2"), max_length=15)
    submit = models.CharField(_("Submit"), max_length=15)
    class Meta:
        verbose_name = 'NewsLetters'
        verbose_name_plural = 'NewsLetters'   
        
        def __str__(self):
            return self.title
