from django.shortcuts import render
from . import forms
from . import models
import accounts
import Blog.models as from_Blog
import accounts.models as from_accounts
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,TemplateView,FormView
from django.views import generic
from django.utils.http import is_safe_url
from django.utils.decorators import method_decorator

"""##########################################################################################################"""

def Index(request):
    return render (request,"stage/index.html")

"""##########################################################################################################"""

def About(request):
    return render(request, 'stage/About.html')

"""##########################################################################################################"""

def Products(request):
    return render(request,"stage/Apps.html")

"""##########################################################################################################"""

def Game01(request):
    return render(request,"stage/Game01/Game01.html")

"""##########################################################################################################"""

def Donate(request):
    return render(request,"stage/Donate.html")

"""##########################################################################################################"""

class UserCreateView(CreateView): #Register User
    # form_class = forms.User_Form
    form_class = forms.UserCreateForm
    # form_class = accounts.forms.RegisterForm
    success_url = reverse_lazy("stage:Main_Page")
    template_name = "registration/register.html"

"""##########################################################################################################"""

#log_in ClassBase View Version
class LoginView(FormView):
    form_class = accounts.forms.LoginForm
    success_url = reverse_lazy("stage:Main_Page")
    template_name = "registration/login.html"

    def form_valid(self,form):
        request = self.request

        next = request.GET.get("next")
        next_ = request.POST.get("next")
        redirect_path = next or next_ or None

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request,email = email ,password=password)

        if user is not None:
            login(request,user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(request_path)
            else:
                return redirect("/")
        return super(LoginView,self).form_invalid(form)

"""##########################################################################################################"""

@login_required
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse("stage:Main_Page"))

"""##########################################################################################################"""

class Profile(generic.TemplateView):
    template_name = "stage/user_profile_detail.html"

    def get_context_data(self,**kwargs):
        # print(self.request.user)
        context = super().get_context_data(**kwargs)
        selected_user_object = from_accounts.User.objects.all().filter(pk=self.kwargs.get("pk")) # .filter(username=self.request.user)
        list_of_post_by_user = from_Blog.Post.objects.all().filter(author=selected_user_object[0])
        q = self.request.GET.get("q")
        if q:
            context["posts"] =list_of_post_by_user.filter(title__icontains=q)
        else:
            context["posts"] = list_of_post_by_user
        context["object"] = selected_user_object
        return context


"""################################################################################################################"""
# def log_in(request):
#     form = accounts.forms.LoginForm(request.POST or None)
#     context = {
#         "form":form
#     }
#     next = request.GET.get("next")
#     next_ = request.POST.get("next")
#     redirect_path = next or next_ or None
#     if form.is_valid():
#         #log in
#         email = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("password")
#         user = authenticate(request,email = email ,password=password)
#         if user is not None:
#             login(request,user)
#             try:
#                 # del request.session("guest_email_id")
#                 pass
#             except:
#                 pass
#             if is_safe_url(redirect_path, request.get_host()):
#                 return redirect(request_path)
#             else:
#                 return redirect("/")
#         else:
#             # print("Error")
#             pass
#     return render(request,"registration/login.html",context)
