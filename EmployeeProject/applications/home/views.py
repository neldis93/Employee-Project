from django.shortcuts import render

from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
)
#importar models
from .models import Test
from .forms import TestForm

# vistas basadas en clases y utilizaremos vistas genericas (TemplateView, ListView, CreateView, UpdateView, etc...  )

class TestView(TemplateView):
    template_name= 'home/test.html'


class TestListView(ListView): 
    template_name = 'home/list.html'
    context_object_name= 'ListNumbers'
    queryset= ['0','10','20','30']


class ToListView(ListView):
    template_name= 'home/list_test.html'
    model= Test # con este paramentro model indicamos a que clase hacemos referencia de models.py para listar
    context_object_name= 'to_list_view'


class TestCreateView(CreateView):
    template_name = "home/add.html"
    model = Test
    #fields=['title','subtitle', 'quantity']
    form_class= TestForm
    success_url= ('/')


# Aplicando el frameswork de CSS Foundation

class SummaryFoundationView(TemplateView):
    template_name= 'home/summary_foundation.html'

