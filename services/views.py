from django.shortcuts import render, get_object_or_404

from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse

from django.db.models import Q


from .models import ImageHeader, Service




def service_list(request):
    index_page = ImageHeader.objects.all()
    service1 = Service.objects.filter(parts__title='part1').order_by('timestamp')
    service2 = Service.objects.filter(parts__title='part2').order_by('timestamp')
    service3 = Service.objects.filter(parts__title='part3').order_by('timestamp')
    service4 = Service.objects.filter(parts__title='part4').order_by('timestamp')
    service5 = Service.objects.filter(parts__title='part5').order_by('timestamp')
    service6 = Service.objects.filter(parts__title='part6').order_by('timestamp')
    service7 = Service.objects.filter(parts__title='part7').order_by('timestamp')
    # service = Service.objects.all()
    template = 'services/list_view.html'
    context ={
        "index_page": index_page,
        "service3": service3,
        "service1": service1,
        "service2": service2,
        "service4": service4,
        "service5": service5,
        "service6": service6,
        "service7": service7,
    }
    return render(request, template, context)


def service_detail(request, slug=None):
    # service1 = Service.objects.all()
    service1 = Service.objects.filter(parts__title='part1').order_by('timestamp')
    service2 = Service.objects.filter(parts__title='part2').order_by('timestamp')
    service3 = Service.objects.filter(parts__title='part3').order_by('timestamp')
    service4 = Service.objects.filter(parts__title='part4').order_by('timestamp')
    service5 = Service.objects.filter(parts__title='part5').order_by('timestamp')
    service6 = Service.objects.filter(parts__title='part6').order_by('timestamp')
    service7 = Service.objects.filter(parts__title='part7').order_by('timestamp')
    try:
        service = get_object_or_404(Service, slug=slug)
    except Service.MultipleObjectsReturned:
        service = Service.objects.filter(slug=slug).order_by('title').first()

    template = 'services/detail_view.html'
    context ={
        "service1": service1,
        "service2": service2,
        "service3": service3,
        "service": service,
        "service4": service4,
        "service5": service5,
        "service6": service6,
        "service7": service7,
    }
    return render(request, template, context)