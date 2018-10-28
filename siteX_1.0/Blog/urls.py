from django.urls import path
from . import views
urlpatterns = [
    #path('login/login.cgi',views.index, name = "Main Page"),
    path('',views.index, name = "Main Page"),
    path('About',views.About, name = "About Page"),
]