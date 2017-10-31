from django.shortcuts import render

import os

from mimetypes import guess_type

from django.conf import settings
from django.utils.encoding import force_bytes
from wsgiref.util import FileWrapper
from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import RegHeaderImage, RegCategory, RegForm




def reg_list(request):
    header = RegHeaderImage.objects.all()
    cat = RegCategory.objects.all()
    template = 'registry/regforms_list.html'
    context = {
        'header': header,
        'cat': cat
    }
    return render(request, template, context)



def reg_detail(request, slug=None):
    header = RegHeaderImage.objects.all()
    try:
        cat_q = get_object_or_404(RegCategory, slug=slug)
    except RegCategory.MultipleObjectsReturned:
        cat_q = RegCategory.objects.filter(slug=slug).order_by('title').first()
    reg_f = cat_q.regform_set.all()
    # reg1 = RegForm.objects.filter(section__title='section1')
    # reg2 = RegForm.objects.filter(section__title='section2')
    template = 'registry/regforms_detail.html'
    context = {
        'header': header,
        'cat_q': cat_q,
        'reg_f': reg_f
    }
    return render(request, template, context)


def reg_download(request):
    pass