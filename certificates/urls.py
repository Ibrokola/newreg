from django.conf.urls import url
from django.contrib import admin

from .views import cert_list, cert_detail

urlpatterns = [
    url(r'^$', cert_list, name='cert_list'),
    url(r'^(?P<slug>[\w-]+)/$', cert_detail, name='cert_detail')
]