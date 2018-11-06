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
class Login_form(forms.ModelForm):
    class Meta:
        model = Login_info
        fields = [
            'username',
            'password',
        ]