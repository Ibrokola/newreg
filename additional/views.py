from django.shortcuts import render

from .models import AddHeader, AddCategory, DaysClosed, Calender



def extra_list(request):
    header = AddHeader.objects.all()
    cat = AddCategory.objects.all()
    closed = DaysClosed.objects.all() 
    calender = Calender.objects.all().order_by('-updated')
    template = 'additional/extra.html'
    context = {
        'header': header,
        'cat': cat,
        'closed': closed,
        'calender': calender
    }
    return render(request, template, context)