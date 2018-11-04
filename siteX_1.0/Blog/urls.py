from django.urls import path
from . import views
urlpatterns = [
    #path('login/login.cgi',views.index, name = "Main Page"),
    path('',views.index, name = "Main Page"),
    path('About.html/',views.About, name = "About Page"),
    path('Contacts.html/',views.Contacts, name='Contacts Page'),
    path('Signup.html/', views.Signup, name= 'Signup Page'),
    path('Login.html/', views.Login, name = "Login Page"),
]