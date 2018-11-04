from django.shortcuts import render

# Create your views here.
#from .models import account_information, blog_content, favorite_information

def index(request):
    """users = account_information.objects.order_by("user_id")
    output = [s.user_id for s in users]"""
    return render(request,'html/index.html')

def About(request):
    return render(request,'html/About.html')

def Contacts(request):
    return render(request, 'html/Contacts.html')

def Login(request):
    return render(request, 'html/Login.html')

def Signup(request):
    return render(request, 'html/Signup.html')

