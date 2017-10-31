from django.db import models

from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save
from django.utils.translation import ugettext_lazy as _

from django.utils.text import slugify
from .utils import create_slug



class AboutHead(models.Model):
    title = models.CharField(max_length=350)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.title)


class About(models.Model):
    title = models.CharField(max_length=300)
    # slug = models.SlugField(blank=True, null=True)
    sub_title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000, default='Hello')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) #time added
    updated = models.DateTimeField(auto_now_add=False, auto_now=True) #time updated

    class Meta:
        verbose_name = _("about")


    def __str__(self):
        return str(self.title)

    # def get_absolute_url(self):
    #     return reverse("about:detail",kwargs={"slug": self.slug})

# def about_pre_save_reciever(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)

# pre_save.connect(about_pre_save_reciever, sender=About)

class AboutAdTitle(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class AboutAdImage(models.Model):
    title = models.ForeignKey(AboutAdTitle)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.title)