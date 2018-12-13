from django.shortcuts import render
from django import forms
from django.http import HttpResponse
# Create your views here.
from .forms import Signup_form, Login_form, Photo
from .models import User, Login_info, Photos
import braintree

# Implementing Braintree Payment API

# Send a client token to your client
# @app.route("/client_token", methods=["GET"])
# def client_token():
#     return gateway.client_token.generate()

## Donate Page
def Donate(request):
    # configure the environment and API credentials:
    gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="vtfnkmt8xmfbxyzc",
        public_key="dhpsqrhxfgqc3zxt",
        private_key="cbe2dbb0a89b34316bdfad583dadb962"
        )
    )
    # Generate a client token
    client_token = gateway.client_token.generate({
    "customer_id": "johnj2015",
    })
    # Send a client token to your client
    context = {
        "CLIENT_TOKEN_FROM_SERVER": client_token,
    }
    # Receive a payment method nonce from your client
    if (request.method == "POST"):
        nonce_from_the_client = "2be624d2-c320-036f-6f6c-322f9000e8b6"
        result = gateway.transaction.sale({
            "amount": request.POST.get("amount"),
            "payment_method_nonce": nonce_from_the_client
        })


    # if (result.is_success):
    #         return HttpResponse("Sucessful")
    # else:
    #     print("Eoor")


    return render(request,"html/Donate.html",context)

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

## About Page
def About(request):
    context = {
    }
    return render(request, 'html/About.html',context)

## Blog Page
def Blogs(request):
    query = request.GET.get("q")
    if query :
        query_list = Photos.objects.all().in_bulk()
        context = {
        "image": (query_list["yumi"].pic.url.split("/")[-1]),
        }
        return render(request,"html/Search_result.html",context)
    return render(request,"html/TableofContent.html")

## Apps page
def Products(request):
    return render(request,"html/Apps.html")
## Game 01
def Game01(request):
    return render(request,"html/Game01/Game01.html")

## Table of Contents page
def TableofContent(request):
    return render(request,'html/TableofContent.html')

## Article-1 ##
def Article_1(request):
    return render(request,"html/Article_1.html")
