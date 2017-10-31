from django.conf.urls import url
from django.contrib import admin

from .views import about

urlpatterns = [
    url(r'^$', about, name='about')
]