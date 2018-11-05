from django.urls import path
from .views import index, About
urlpatterns = [
    path('About/',About, name = "About Page"),
    path('',index, name = "Main Page"),
]