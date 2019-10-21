from django.shortcuts import render
from django.views import View
from django.views.generic import *
from . import models
from . import forms
# Create your views here.

# def index(request):
#     return render(request,"hal_il/index.html")

class List_Task(TemplateView):
    template_name = "hal_il/index.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context["number_of_tasks"] = models.Task.objects.all().count
        context["Tasks"] = models.Task.objects.all()
        return context


# class List_Task(View):
#     context = {
#         "number_of_tasks": models.Task.objects.all().count,
#         "Tasks": models.Task.objects.all(),
#     }
#     def get(self,request,*args, **kwargs):
#         return render(request,"hal_il/index.html",self.context)

class Task_View(CreateView):
    template_name_suffix = "_create"
    form_class = forms.Task_Form
    model = models.Task
    redirect_field_name = "hal_il/index.html"
