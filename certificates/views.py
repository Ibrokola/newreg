from django.shortcuts import render, get_object_or_404

from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse

from django.db.models import Q


from .models import CertHeader, CertCategory




def cert_list(request):
    index_page = CertHeader.objects.all()
    cert = CertCategory.objects.all()
    template = 'certificates/list_view.html'
    context ={
        "index_page": index_page,
        "cert": cert
    }
    return render(request, template, context)


def cert_detail(request, slug=None):
    cert1 = CertCategory.objects.all()
    try:
        cert = get_object_or_404(CertCategory, slug=slug)
    except CertCategory.MultipleObjectsReturned:
        cert = CertCategory.objects.filter(slug=slug).order_by('title').first()

    template = 'certificates/detail_view.html'
    context ={
        "cert1": cert1,
        "cert": cert
    }
    return render(request, template, context)

