from django.shortcuts import render,HttpResponseRedirect,redirect
from django.views import View
from django.views.generic import *
from . import models
from . import forms
# import json
from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404,redirect
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


def Update_Task(request):
    if request.is_ajax():
        try:
            del_pk = request.POST["item_pk"]
            if del_pk:
                task = get_object_or_404(models.Task,pk=del_pk[-2:])
                task.action_check()
                return reverse_lazy("hal_il:Main_Page")
        except KeyError:
            pass
    else:
        pass
    return reverse_lazy("hal_il:Main_Page")





def Delete_Task(request):
    checked_tasks = models.Task.objects.all().filter(is_checked = True)
    checked_tasks.delete()
    return redirect("hal_il:Main_Page")
