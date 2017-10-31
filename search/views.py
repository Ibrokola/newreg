from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View

from certificates.models import CertCategory
from services.models import Service
from registry.models import RegCategory, RegForm



class SearchView(View):
    def get(self, request, *args, **kwargs):
        template = "search/default.html"
        query = request.GET.get('q')
        qs = None
        s_qs = None
        r_qs = None
        if query:
            ep_lookup = Q(title__icontains=query)

            serv_lookup = ep_lookup | Q(title__icontains=query) | Q(title__iexact=query) 

            reg_lookup = ep_lookup | Q(category__title__icontains=query) | Q(title__icontains=query) | Q(title__iexact=query) 
            cert_lookup = ep_lookup | Q(title__icontains=query)

            qs = CertCategory.objects.all().filter(cert_lookup).distinct()
            
            s_qs = Service.objects.filter(ep_lookup | serv_lookup)
            r_qs = RegForm.objects.filter(ep_lookup | reg_lookup)
        context = {"qs":qs, "s_qs":s_qs, "r_qs":r_qs}
        return render(request, template, context)