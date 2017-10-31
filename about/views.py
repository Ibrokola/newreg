from django.shortcuts import render

from .models import AboutHead, About, AboutAdTitle, AboutAdImage


def about(request):
    abhead = AboutHead.objects.all()
    abt = About.objects.all()
    abad1 = AboutAdTitle.objects.all()
    abad2 = AboutAdImage.objects.all()
    template = 'about/about.html'
    context = {
        'abhead': abhead,
        'abt': abt,
        'abad1': abad1,
        'abad2': abad2
    }
    return render(request, template, context)