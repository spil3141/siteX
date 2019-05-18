from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,ListView,DeleteView,UpdateView
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


class Delete_DeleteView(DeleteView):
    template_name_suffix = "_confirm_delete"
    model = models.Words_Bank
    success_url = reverse_lazy("helper:Main_Page")


class Update_UpdateView(UpdateView):
    model = models.Words_Bank
    fields = ["kor_word", "eng_word"]
