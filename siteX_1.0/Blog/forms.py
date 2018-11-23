from django import forms 

from .models import User, Login_info, Photos

class Signup_form(forms.Form):
    user_ID = forms.CharField( label= "Username", max_length=30,widget= forms.TextInput(attrs={'class': 'text-color'}))
    user_password = forms.CharField(label="Password", max_length=30,widget=forms.PasswordInput(attrs={'type':'password','class':'text-color'}))
    about = forms.CharField(required = False, widget=forms.Textarea( attrs={'rows':'2','class':'text-color'}))

class Login_form(forms.Form):
    username = forms.CharField(label= "Username",max_length=100,widget= forms.TextInput(attrs={'class': 'text-color'}))
    password = forms.CharField(label="Password",max_length=20, widget=forms.PasswordInput(attrs={ "type":"password",'class':'text-color'}))

class Photo(forms.Form):
    name = forms.CharField(max_length = 30,widget= forms.TextInput(attrs={'class': 'text-color'}))
    upload_pic = forms.ImageField()

