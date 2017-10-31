from django.db import models


from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator


class ContactHeader(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=300)

    def __str__(self):
        return str(self.title)


# class Contact(models.Model):
#     name = models.CharField(max_length=300)
#     email = models.EmailField(max_length=300)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone_no = models.CharField(validators=[phone_regex], max_length=20, blank=True, null=True)
#     message = models.TextField(max_length=None)

#     def __str__(self):
#         return str(self.name)

class DriversGuide(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    d_link = models.CharField(max_length=1000, null=True, blank=True)
    other_link = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return str(self.title)