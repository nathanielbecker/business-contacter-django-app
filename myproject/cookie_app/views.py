from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import Initial_Borr_List_PageForm
from .models import Initial_Borr_List_Page

##you added this
from django.http import HttpResponse
# from django.shortcuts import render ##this is for django_tables2
from tablify import SimpleTable
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
###

class Initial_Borr_List_PageList(ListView):
    model = Initial_Borr_List_Page
    paginate_by = 20


class Initial_Borr_List_PageCreate(CreateView):
    model = Initial_Borr_List_Page
    form_class = Initial_Borr_List_PageForm
    success_url = reverse_lazy('Initial_Borr_List_Page_list')


class Initial_Borr_List_PageDetail(DetailView):
    model = Initial_Borr_List_Page


class Initial_Borr_List_PageUpdate(UpdateView):
    model = Initial_Borr_List_Page
    form_class = Initial_Borr_List_PageForm
    success_url = reverse_lazy('Initial_Borr_List_Page_list')


class Initial_Borr_List_PageDelete(DeleteView):
    model = Initial_Borr_List_Page
    success_url = reverse_lazy('Initial_Borr_List_Page_list')

# def tablify(request):
#     return render(request, "cookie_app/tablify.html", {"tablify": Initial_Borr_List_Page.objects.all()})

def tablify(request):
    queryset = Initial_Borr_List_Page.objects.all()
    table = SimpleTable(queryset)
    return render_to_response("cookie_app/tablify.html", {"table": table},
                              context_instance=RequestContext(request))