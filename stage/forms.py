from django import forms
import accounts
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
# from .models import User_Profile
# class User_Form(UserCreationForm):
#     class Mete:
#         model = get_user_model()
#         fields = ["username","email","password1","password2"]

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("photo","username", "email", "password1", "password2","about")
        model = accounts.models.User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
