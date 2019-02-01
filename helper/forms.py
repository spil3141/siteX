from django import forms
from .models import Words_Bank

class Words_Form(forms.ModelForm):
    class Meta:
        model = Words_Bank
        fields = "__all__"
