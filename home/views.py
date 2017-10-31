from django.shortcuts import render
import time


from .models import HomeCarousel, Marketing, HomeIntro, Reminder

def home(request):
    carousel = HomeCarousel.objects.all()
    localtime = time.asctime(time.localtime(time.time()))
    market = Marketing.objects.all().order_by('?')
    intro = HomeIntro.objects.all()
    remind = Reminder.objects.all().order_by('?')
    context = {
        "localtime": localtime,
        "carousel": carousel,
        "market": market,
        "intro": intro,
        "remind":remind,
    }
    template = "home/home.html"
    return render(request, template, context)