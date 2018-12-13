#Contains Django path Function
from django.urls import path

# Importing the Various View Functions from our app's "views.py" file
from .views import index, About, Signup, Login, Image, Blogs, Products, Game01 , Donate, TableofContent , Article_1

# Out app's URLs Array

urlpatterns = [
    path("Game01/", Game01, name = "Game Number 1"),
    path("Article_1/",Article_1, name="Boolean Algebra Article"),
    path("TableofContent/",TableofContent, name="Blogs Table of Content Page"),
    path("Donate/",Donate, name="Donating page"),
    path("Apps/",Products, name = "Products page"),
    path("Blogs/",Blogs, name = "Blog page"),
    path('Image/',Image, name = "Images and files plage" ),
    path('Login/', Login , name = "Log in Page"),
    path('Signup/', Signup, name = "Sign up Page" ),
    path('About/',About, name = "About Page"),
    path('',index, name = "Main Page"),
]
