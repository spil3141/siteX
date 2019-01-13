from django.shortcuts import render

def Signup(request):
    return render(request,"registration/register.html")
