from django.contrib import admin

from .models import CertHeader, CertCategory


admin.site.register(CertHeader)
admin.site.register(CertCategory)