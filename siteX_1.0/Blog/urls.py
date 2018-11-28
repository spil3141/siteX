from django.urls import path

from .views import index, About, Signup, Login, Image, Blog, Apps, Donate

urlpatterns = [
    path("Donate/",Donate, name="Donating page"),
    path("Apps/",Apps, name = "Products page"),
    path("Blog/",Blog, name = "Blog page"),
    path('Image/',Image, name = "Images and files plage" ),
    path('Login/', Login , name = "Log in Page"),
    path('Signup/', Signup, name = "Sign up Page" ),
    path('About/',About, name = "About Page"),
    path('',index, name = "Main Page"),
]