from django.db import models

from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save
from django.utils.translation import ugettext_lazy as _

from django.utils.text import slugify
from about.utils import create_slug



class AddHeader(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    # description = models.TextField(max_length=None)

    def __str__(self):
        return str(self.title)



class DaysClosed(models.Model):
    title = models.CharField(max_length=200)
    days = models.TextField(max_length=None, null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Calender(models.Model):
    img = models.ImageField(upload_to='images/')
    # pos = models.CharField(max_length=300, default = 'Jan')
    order = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=300)
    desc = models.TextField(max_length=None)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) #time added
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return str(self.title) 



class AddCategory(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=None)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return str(self.title)
    
    # def get_absolute_url(self):
    #     return reverse("additional:detail",kwargs={"slug": self.slug})

def add_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(add_pre_save_reciever, sender=AddCategory)