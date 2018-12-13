#Contains Django path Function
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

# Importing the Various View Functions from our app's "views.py" file
from .views import (
    index,
    About,
    Signup,
    Login,
    Image,
    Blogs,
    Products,
    Game01 ,
    Donate,
    TableofContent ,
    Article_1,
    )

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



## Still Learning




# If you use django.contrib.staticfiles as explained above, runserver will do this automatically
# when DEBUG is set to True. If you don’t have django.contrib.staticfiles in INSTALLED_APPS, you
# can still manually serve static files using the django.views.static.serve() view.
# This is not suitable for production use! For some common deployment strategies, see Deploying static files.
#
# if (settings.DEBUG):
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
