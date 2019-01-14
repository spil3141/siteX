from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from . import models
from . import forms
from django.conf import settings
import numpy as np
import os
import PIL
from PIL import Image
from sklearn.externals import joblib
import numpy
from PIL import Image
from . import DataPreprocessing as spil
from django.views.generic import (CreateView,
                                  DetailView,
                                  ListView,
                                  TemplateView
                                  )



class Success(DetailView):
    model = models.Item
    if (os.system("uname -r") == "17.7.0"):
        clf = joblib.load("detector/static/detector/externals/Trained_Model.sav")
    elif (os.system("uname -r") == "4.4.0-1072-aws"):
        clf = joblib.load("Desktop/siteX/detector/static/detector/externals/Trained_Model.sav")

    def get_object(self):
        obj = super().get_object()

        #Converting img to numpy 1d array
        img = spil.img_2_1d_arr(obj.image)

        #using the classifier to make prediction
        if self.clf:
            self.prediction = str(self.clf.predict([img])[0])
            self.prob = self.clf.predict_proba([img]) % 10
        else:
            self.prediction = "failed to load"
            self.prob = "error"

        return obj

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["prediction"] = self.prediction
        context["prob"] = self.prob
        return context


class History(ListView):
    context_object_name = "items"
    model = models.Item


class Index(TemplateView):
    template_name = "detector/index.html"


class Upload(CreateView):
    template_name_suffix = "_create"
    form_class = forms.ItemForm
    template_name = "detector/item_create.html"

    # success = False
    # if request.method == "POST":
    #     form = forms.ItemForm(request.POST, request.FILES)
    #     if (form.is_valid()):
    #         form.save(commit=True)
    #         success = True
    #         resizer(form.cleaned_data["name"])
    #         form = forms.ItemForm()
    # else:
    #     form = forms.ItemForm()
    # return render(request,"detector/Upload.html",{"form":form,"success":success})



# This function resize the image uploaded by users to 300 pixels width and prepotional height
def resizer(filename):
    dir_path = settings.BASE_DIR + "/media/detector/Images/"
    for file in os.listdir(dir_path):
        if file == filename:
            img = Image.open(dir_path + file)
            basewidth = 300
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
            img.save(dir_path + file)
