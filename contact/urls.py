from django.conf.urls import url
from django.contrib import admin

from .views import driver_list

urlpatterns = [
    url(r'^$', driver_list, name='driver_list'),
]