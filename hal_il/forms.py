from django import forms
from . import models
#
# class List_Form(forms.ModelForm):
#     class Meta:
#         model = models.List
#         fields = ["__all__"]

class Task_Form(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ["content"]
