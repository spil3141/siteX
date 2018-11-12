from django import forms 

from .models import User, Login_info

class Signup_form(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'user_ID',
            'user_password',
            'about',
        ]
class Login_form(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=20)
