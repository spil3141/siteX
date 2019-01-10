from django import forms
from Blog.models import Post, Comment

class Post_Form(forms.ModelForm):
    class Meta:
        model= Post
        fields = ["author","title","text"]

        widgets = {
        "title": forms.TextInput(attrs= {"class":"textinputclass"}),
        "text" : forms.Textarea(attrs= {"class":"loader editable medium-editor-textarea postcontent"}),
        }
class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author","text")

        widgets = {
        "author": forms.TextInput(attrs= {"class":"textinputclass"}),
        "text": forms.Textarea(attrs= {"class":"editable medium-editor-textarea"}),
        }
