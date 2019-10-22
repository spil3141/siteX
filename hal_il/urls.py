
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import url
from . import views

app_name = "hal_il"

urlpatterns = [
    path("",views.List_Task.as_view(),name="Main_Page"),
    path("task/create",views.Task_View.as_view(),name="Create_Task"),
    re_path("task/update",views.Update_Task,name = "Update_Task"),
    path("task/delete/",views.Delete_Task,name="Delete_Task"),
]
