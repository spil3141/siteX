from django.urls import path
from . import views

app_name = "CCTV"
urlpatterns = (
    path("", views.Index, name="CCTV_Page"),
)
