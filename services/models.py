from django.db import models

from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save
from django.utils.translation import ugettext_lazy as _

from django.utils.text import slugify
from about.utils import create_slug


class ImageHeader(models.Model):
    image = models.ImageField(upload_to='images/')
    # service = models.ForeignKey('Service', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    intro = models.TextField(max_length=None)


    def __str__(self):
        return str(self.title)

class Part(models.Model):
    title = models.CharField(max_length=500)
    # title2 = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)


class Service(models.Model):
    parts = models.ForeignKey(Part)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) #time added
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    description = models.TextField(max_length=None, blank=True, null=True)
    external_link = models.CharField(max_length=300, null=True, blank=True)
    external_link2 = models.CharField(max_length=300, null=True, blank=True)
    external_link3 = models.CharField(max_length=300, null=True, blank=True)
    external_link4 = models.CharField(max_length=300, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)


    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("services:service_detail",kwargs={"slug": self.slug})

def service_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(service_pre_save_reciever, sender=Service)