from django.db import models




class HomeCarousel(models.Model):
    image       = models.ImageField(upload_to='images/')
    title       = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return str(self.title)

class HomeIntro(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    intro = models.TextField(max_length=None)

    def __str__(self):
        return str(self.title)

class Reminder(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    button_remind = models.CharField(max_length=500, blank=True, null=True)
    button_renew = models.CharField(max_length=500, blank=True, null=True)
    car_test = models.CharField(max_length=500, blank=True, null=True)
    car_proof = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.title)

class Marketing(models.Model):
    image   = models.ImageField(upload_to='images/')
    title   = models.CharField(max_length=200, null=True, blank=True)
    description  = models.TextField(max_length=3000, null=True, blank=True) 
    read_more = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.title) 