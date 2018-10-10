from django.shortcuts import render

# Create your views here.
from . import models

def index(request):
    users = models.account_information.object.all()
    return render(request,'html/index.html',{"users_all": users})

def About(request):
    return render(request,'html/About.html')


