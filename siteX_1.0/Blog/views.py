from django.shortcuts import render
from django import forms
from django.http import HttpResponse
# Create your views here.
from .forms import Signup_form, Login_form, Photo
from .models import User, Login_info, Photos

##   MAIN View
def index(request):
    data = User.objects.all().in_bulk() #Selecting all the Queryset form the database 
    context = {
        'data' : data.keys(),
    }
    return render(request,'html/index.html',context)

## Media View
def Image(request):
    if request.method == "POST":
        pic = Photo(request.POST,request.FILES)
        if pic.is_valid():
            if not Photos.objects.filter(photo_ID = pic.cleaned_data['name']):
                Photos.objects.create(photo_ID = pic.cleaned_data['name'], pic = pic.cleaned_data['upload_pic'])
            else:
                pass
    else:
        pic = Photo()
    context = {
        'var' : pic,
    }
    return render(request,"html/Image.html",context)

## Sign up View
def Signup(request):
    test = 0
    if request.method == "POST":
        signup_form = Signup_form(request.POST)
        if signup_form.is_valid():
            if signup_form.cleaned_data['user_ID'] not in User.objects.all().in_bulk().keys():
                #User.objects.create(user_ID = signup_form.cleaned_data['user_ID'],user_password = signup_form.cleaned_data['user_password'], about= signup_form.cleaned_data['about'])
                users = User(
                user_ID = signup_form.cleaned_data['user_ID'],
                user_password = signup_form.cleaned_data['user_password'],
                about= signup_form.cleaned_data['about']
                )
                users.save()
                test = 2
            else:
                test = 1
    signup_form = Signup_form()
    context = {
        'signup_var': signup_form,
        'test': test
    }
    return render(request,'html/Signup.html', context)

## Login View
def Login(request):
    if request.method == "POST":
        login_form = Login_form(request.POST)
        if login_form.is_valid():
            # filter() returns True if the filter value is in the database 
            if login_form.cleaned_data["username"] == "spil3141" and login_form.cleaned_data["password"] == "asdf":
                return render(request, "html/spil3141.html")
            elif User.objects.filter(user_ID = login_form.cleaned_data["username"]) and User.objects.filter( user_password = login_form.cleaned_data['password']):
                return render(request,"html/DefaultLogin.html")
    login_form = Login_form()
    context = {
        'login_var': login_form,
        }
    return render(request,'html/Login.html', context)

def About(request):
    context = {
    }
    return render(request, 'html/About.html',context)

def Blog(request):
    return render(request,"html/Blogs.html")

def Apps(request):
    return render(request,"html/Apps.html")

def Donate(request):
    return render(request,"html/Donate.html")
