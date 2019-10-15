from django.urls import path,re_path
from django.conf.urls import url
# from .views import (Index,About,
#                     Products,Game01,
#                     Donate,UserCreateView
#                     )
from . import views

app_name = "stage"

urlpatterns = [
    path("Game01/", views.Game01, name = "Game"),
    path("Donate/",views.Donate, name="Donate_Page"),
    path("Apps/",views.Products, name = "App_Page"),
    path('About/',views.About, name = "About_Page"),
    path("",views.Index, name="Main_Page"),
    path("accounts/signup/",views.UserCreateView.as_view(),name="Signup_Page"),
    # url(r"^account/profile/$",views.Profile.as_view(),name="Profile"),
]
