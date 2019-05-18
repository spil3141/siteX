from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class User_Form(UserCreationForm):
    class Mete:
        model = get_user_model()
        fields = ["username","email","password1","password2"]
