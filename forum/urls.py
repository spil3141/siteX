from django.urls import path,re_path
from django.conf.urls import url
from . import views

app_name = "forum"

urlpatterns = [
    path("",views.index,name="Main_Page"),
]
