from django.contrib import messages
from django.shortcuts import render

from django.db.models.signals import post_save, pre_save
from .models import DriversGuide



def driver_list(request):
    drive_g = DriversGuide.objects.all()
    template = 'contact/list_view.html'
    context ={
        "drive_g": drive_g,
    }
    return render(request, template, context)
