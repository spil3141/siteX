from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import Signup_form, Login_form


def index(request):
    return render(request,'html/index.html')

def Signup(request):
    signup_form = Signup_form(request.POST or None)
    if signup_form.is_valid():
        signup_form.save()
        signup_form = Signup_form()
    context = {
        'signup_var': signup_form,
    }
    return render(request,'html/Signup.html', context)

def Login(request):
    login_form = Login_form(request.POST or None)
    if login_form.is_valid():
        login_form.save()
        login_form = Login_form()
    context = {
        'login_var': login_form,
        }
    return render(request,'html/Login.html', context)

def About(request):
    return render(request, 'html/About.html')

