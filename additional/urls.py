from django.conf.urls import url
from django.contrib import admin

from .views import extra_list

urlpatterns = [
    url(r'^$', extra_list, name='extra_list')
]