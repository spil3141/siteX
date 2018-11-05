from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#from .models import account_information, blog_content, favorite_information

def index(request):
    """users = account_information.objects.order_by("user_id")
    output = [s.user_id for s in users]"""
    return render(request,'html/index.html')
def About(request):
    return render(request, 'html/About.html')


