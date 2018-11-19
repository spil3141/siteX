from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import Signup_form, Login_form
from .models import User, Login_info

def index(request):
    data = User.objects.all().in_bulk()

    context = {
        'data' : data.keys()
    }
    return render(request,'html/index.html',context)

def Signup(request):
    test = 0
    if request.method == "POST":
        signup_form = Signup_form(request.POST)
        if signup_form.is_valid():
            print (signup_form.cleaned_data)
            print ('There are %d Users' % (User.objects.count())) # returns an integer representing the number of element in the db
            print (User.objects.all().in_bulk())  #Return a dictionary mapping each of the given IDs to the object with that ID.
            if signup_form.cleaned_data['user_ID'] not in User.objects.all().in_bulk().keys():
                User.objects.create(user_ID = signup_form.cleaned_data['user_ID'],user_password = signup_form.cleaned_data['user_password'], about= signup_form.cleaned_data['about'])
                print ('Created new User Successfully!')
                test = 2
            else:
                print ("User already exists in the database ! ")
                test = 1
                #raise ValidationError(_('User already exists'), code='invalid')
    signup_form = Signup_form()
    context = {
        'signup_var': signup_form,
        'test': test
    }
    return render(request,'html/Signup.html', context)

def Loggedin(request):
    return HttpResponse("You are Logged in !!!")

def Login(request):
    login_form = Login_form()
    context = {
        'login_var': login_form,
        }
    return render(request,'html/Login.html', context)

def About(request):
    context = {
    }
    return render(request, 'html/About.html',context)

