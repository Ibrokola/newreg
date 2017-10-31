from django.db import models

from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save
from django.utils.translation import ugettext_lazy as _

from django.utils.text import slugify
from about.utils import create_slug





class RegHeaderImage(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    intro = models.TextField(max_length=None)

    def __str__(self):
        return str(self.title)
    
    # def get_absolute_url(self):
    #     return reverse("forms:detail")

class RegCategory(models.Model):
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)
    new_link = models.CharField(max_length=1000, null=True, blank=True)
    # title2 = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('reg:reg_detail', kwargs={"slug": self.slug})



def cat_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(cat_pre_save_reciever, sender=RegCategory)

class RegForm(models.Model):
    # header = models.ForeignKey(RegHeaderImage, related_name='page_header')
    category = models.ForeignKey(RegCategory)
    title = models.CharField(max_length=1000)
    slug = models.SlugField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) #time added
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #last saved
    # download_file = models.FileField(null=True, blank=True)
    ext_link = models.CharField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return str(self.title)

    # def get_absolute_url(self):
	# 	return reverse('forms:reg_detail', kwargs={"reg_slug": self.slug, "cat_slug": self.category.slug})


def reg_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(reg_pre_save_reciever, sender=RegForm)