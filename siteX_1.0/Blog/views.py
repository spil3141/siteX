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
                print ("Successfully Uploaded")
            else:
                print ("Error Uploading")
    else:
        pic = Photo()
    
    return render(request,"html/Image.html",{'var' : pic })

## Sign up View
def Signup(request):
    test = 0
    if request.method == "POST":
        signup_form = Signup_form(request.POST)
        if signup_form.is_valid():
            #print (signup_form.cleaned_data)
            #print ('There are %d Users' % (User.objects.count())) # returns an integer representing the number of element in the db
            #print (User.objects.all().in_bulk())  #Return a dictionary mapping each of the given IDs to the object with that ID.
            if signup_form.cleaned_data['user_ID'] not in User.objects.all().in_bulk().keys():
                #User.objects.create(user_ID = signup_form.cleaned_data['user_ID'],user_password = signup_form.cleaned_data['user_password'], about= signup_form.cleaned_data['about'])
                users = User(
                user_ID = signup_form.cleaned_data['user_ID'],
                user_password = signup_form.cleaned_data['user_password'],
                about= signup_form.cleaned_data['about']
                )
                users.save()
                print ('Created new User Successfully!')
                test = 2
            else:
                #print ("User already exists in the database ! ")
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
            if User.objects.filter(user_ID = login_form.cleaned_data["username"]) and User.objects.filter( user_password = login_form.cleaned_data['password']):
                return HttpResponse("You are Logged In !!")
    else:
        print ("Couldnt log in ")
        #raise forms.ValidationError("User not Found!")
    login_form = Login_form()
    context = {
        'login_var': login_form,
        }
    return render(request,'html/Login.html', context)

def About(request):
    context = {
    }
    return render(request, 'html/About.html',context)

