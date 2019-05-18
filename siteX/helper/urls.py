from django.urls import path,re_path
from django.conf.urls import url
from . import views

app_name = "helper"

urlpatterns = [
    path("",views.Index.as_view(), name = "Main_Page"),
    path("new_word/",views.Add_CreateView.as_view(),name ="Create_Page"),
    # re_path(r"^display/(?P<pk>\d+)/$",views.Display_DetailView.as_view(), name = "Display_Page"),
    url(r"^image/(?P<pk>\d+)/$",views.Display_DetailView.as_view(), name = "Display_Page"),
    re_path(r"^(?P<pk>\d+)/delete/$",views.Delete_DeleteView.as_view(), name="Delete_Page"),
    re_path(r"^(?P<pk>\d+)/update/$", views.Update_UpdateView.as_view(), name = "Update_Page"),
]
