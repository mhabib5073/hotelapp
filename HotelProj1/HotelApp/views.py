from django.shortcuts import render
from .models import *
from django.views.generic import *


class Index(TemplateView):
    template_name = 'index.html'

class Table(ListView):
    model = Customer
    template_name = 'table.html'


class Create(CreateView):
    model = Customer
    fields = ('__all__')
    template_name = 'create.html'

class Detail(DetailView):
    model = Customer
    template_name = 'detail.html'

class Delete(DeleteView):
    model = Customer
    template_name = 'delete.html'
