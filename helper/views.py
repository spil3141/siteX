from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView
from . import forms
from . import models
# Create your views here.

class Index(ListView):
    context_object_name = "object"
    model = models.Words_Bank

class Add_CreateView(CreateView):
    template_name_suffix = "_create"
    form_class = forms.Words_Form
    template_name = "helper/card_create.html"
    # model = models.Words_Bank
class Display_DetailView(DetailView):
    model = models.Words_Bank
    context_object_name = "obj"
