from django.urls import path,re_path
from django.conf.urls import url
from .views import (Index,About,
                    Products,Game01,
                    Donate,UserCreateView
                    )
app_name = "stage"

urlpatterns = [
    path("Game01/", Game01, name = "Game"),
    path("Donate/",Donate, name="Donate_Page"),
    path("Apps/",Products, name = "App_Page"),
    path('About/',About, name = "About_Page"),
    path("",Index, name="Main_Page"),
    path("accounts/profile/",Index),
    path("accounts/signup/",UserCreateView.as_view(),name="Signup_Page"),
    # path("signup/",views.Signup,name = "Signup_Page"),
]
