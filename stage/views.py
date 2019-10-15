from django.shortcuts import render
from . import forms
from . import models
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views import generic

def Index(request):
    return render (request,"stage/index.html")

def About(request):
    return render(request, 'stage/About.html')

def Products(request):
    return render(request,"stage/Apps.html")

def Game01(request):
    return render(request,"stage/Game01/Game01.html")

def Donate(request):
    return render(request,"stage/Donate.html")

class UserCreateView(CreateView):
    # form_class = forms.User_Form
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("stage:Main_Page")
    template_name = "registration/register.html"

# class Profile(generic.DetailView):
#     model = models.User_Profile
#     template_name = "user_profile_detail.html"

# def Signup(request):
#     return render(request,"registration/register.html")


# # Implementing Braintree Payment API
# import braintree
# ## Donate Page
# def Donate(request):
#     # configure the environment and API credentials:
#     gateway = braintree.BraintreeGateway(
#     braintree.Configuration(
#         braintree.Environment.Sandbox,
#         merchant_id="vtfnkmt8xmfbxyzc",
#         public_key="dhpsqrhxfgqc3zxt",
#         private_key="cbe2dbb0a89b34316bdfad583dadb962"
#         )
#     )
#     # Generate a client token
#     client_token = gateway.client_token.generate({
#     "customer_id": "johnj2015",
#     })
#     # Send a client token to your client
#     context = {
#         "CLIENT_TOKEN_FROM_SERVER": client_token,
#     }
#     # Receive a payment method nonce from your client
#     if (request.method == "POST"):
#         nonce_from_the_client = "2be624d2-c320-036f-6f6c-322f9000e8b6"
#         result = gateway.transaction.sale({
#             "amount": request.POST.get("amount"),
#             "payment_method_nonce": nonce_from_the_client
#         })
#     return render(request,"html/Donate.html",context)
