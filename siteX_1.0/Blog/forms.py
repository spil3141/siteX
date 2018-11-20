from django import forms 

from .models import User, Login_info, Photos

class Signup_form(forms.Form):
    user_ID = forms.CharField( label= "Username", max_length=30)
    user_password = forms.CharField(label="Password", max_length=30,widget=forms.PasswordInput(attrs={'type':'password'}))
    about = forms.CharField(required = False, widget=forms.Textarea( attrs={'rows':'2'}))

class Login_form(forms.Form):
    username = forms.CharField(label= "Username",max_length=100)
    password = forms.CharField(label="Password",max_length=20, widget=forms.PasswordInput(attrs={ "type":"password"}))

class Photo(forms.Form):
    name = forms.CharField(max_length = 30)
    upload_pic = forms.ImageField()

