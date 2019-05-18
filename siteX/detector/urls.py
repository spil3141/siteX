from django.urls import path,re_path
from django.conf.urls import url
from . import views

app_name = "detector"

urlpatterns = [
    re_path(r"^$",views.Index.as_view(),name="Main_Page"),
    path("upload/",views.Upload.as_view(),name="Upload_Page"),
    url(r"^image/(?P<pk>\d+)/$",views.Success.as_view(), name = "On_Success_Page"),
    path("history/",views.History.as_view(),name="History_Page"),
]
