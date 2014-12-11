from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import barebones_CRUDForm
from .models import barebones_CRUD

##you added this
from django.http import HttpResponse
from django.shortcuts import render ##this is for django_tables2
from tablify import SimpleTable
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
###

class barebones_CRUDList(ListView):
    model = barebones_CRUD
    paginate_by = 20


class barebones_CRUDCreate(CreateView):
    model = barebones_CRUD
    form_class = barebones_CRUDForm
    success_url = reverse_lazy('barebones_crud_list')


class barebones_CRUDDetail(DetailView):
    model = barebones_CRUD


class barebones_CRUDUpdate(UpdateView):
    model = barebones_CRUD
    form_class = barebones_CRUDForm
    success_url = reverse_lazy('barebones_crud_list')


class barebones_CRUDDelete(DeleteView):
    model = barebones_CRUD
    success_url = reverse_lazy('barebones_crud_list')

# def tablify(request):
#     return render(request, "cookie_app/tablify.html", {"tablify": barebones_CRUD.objects.all()})

def tablify(request):
    queryset = barebones_CRUD.objects.all()
    table = SimpleTable(queryset)
    return render_to_response("cookie_app/tablify.html", {"table": table},
                              context_instance=RequestContext(request))