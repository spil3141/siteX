"""siteX_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import url
from django.contrib.auth.views  import login,logout
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("stage.urls")),
    path("Blog/",include("Blog.urls")),
    url(r"accounts/login/$",login,name="Login_Page"),
    url(r"accounts/logout/$",logout,name="Logout_Page",kwargs={"next_page":"/"}),
    path("Detector/",include("detector.urls")),
    path("KWMH/",include("helper.urls")),
    path("CCTV/", include("CCTV.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)