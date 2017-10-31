from django.conf.urls import url
from django.contrib import admin

from .views import service_list, service_detail

urlpatterns = [
    url(r'^$', service_list, name='service_list'),
    url(r'^(?P<slug>[\w-]+)/$', service_detail, name='service_detail')
]