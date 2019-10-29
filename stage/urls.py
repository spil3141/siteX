from django.urls import path,re_path
from django.conf.urls import url
# from .views import (Index,About,
#                     Products,Game01,
#                     Donate,UserCreateView
#                     )
from . import views
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login,logout # dja/ngo 2.2.6


app_name = "stage"

urlpatterns = [
    path("Game01/", views.Game01, name = "Game"),
    path("Donate/",views.Donate, name="Donate_Page"),
    path("Apps/",views.Products, name = "App_Page"),
    path('About/',views.About, name = "About_Page"),
    path("",views.Index, name="Main_Page"),
    path("stage/signup/",views.UserCreateView.as_view(),name="Signup_Page"),
    path("stage/login/",views.LoginView.as_view(),name="Login_Page"),
    re_path(r"^stage/profile/(?P<pk>\d+)$",login_required(views.Profile.as_view()),name="Profile"),
    # re_path(r"^post/search/(?P<pk>\d+)$",views.SearchResultsView.as_view(),name="Search_Result"),
    url(r"logout/$",views.logoutUser,name="Logout_Page"),
    # path("aaaa/",views.logoutpage,name="Thanks_for_Logging_out"),
    path("success/",views.on_sucessful_payment,name="on_sucessful_payment"),
    path("Thanks/",views.ThanksPage,name="Thanks_Page"),
]
# r"^post/(?P<pk>\d+)$"
