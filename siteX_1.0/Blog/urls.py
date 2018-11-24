from django.urls import path

from .views import index, About, Signup, Login, Image, Blog

urlpatterns = [
    path("Blog/",Blog, name = "Blog page"),
    path('Image/',Image, name = "Images and files plage" ),
    path('Login/', Login , name = "Log in Page"),
    path('Signup/', Signup, name = "Sign up Page" ),
    path('About/',About, name = "About Page"),
    path('',index, name = "Main Page"),
]