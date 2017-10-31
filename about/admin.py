from django.contrib import admin

from .models import About, AboutAdTitle, AboutAdImage, AboutHead

admin.site.register(AboutHead)
admin.site.register(About)
admin.site.register(AboutAdTitle)
admin.site.register(AboutAdImage)