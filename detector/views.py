from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
import platform
from . import models
from . import forms
import numpy as np
from sklearn.externals import joblib
from . import DataPreprocessing
import tensorflow as tf
from django.views.generic import (CreateView,
                                  DetailView,
                                  ListView,
                                  TemplateView
                                  )
# /Users/spil3141/Desktop/siteX/detector/static/detector/externals/digits_model_full.sav

# Desktop/siteX/detector/static/detector/externals/digits_model_full.sav


class Success(DetailView):
    model = models.Item
    # Assigning Absolute path based on OS
    if (platform.system() == "Darwin"):
        loaded_model_path = joblib.load("/Users/spil3141/Desktop/siteX/detector/static/detector/externals/Trained_Model.sav")
    elif (platform.system() == "Linux"):
        loaded_model_path = "/home/spil3141/Desktop/siteX/detector/static/detector/externals/MNIST_Model_10EPOCHS.h5"
        weights_path = "/home/spil3141/Desktop/siteX/detector/static/detector/externals/cnn_checkpoint.h5"
        sc_path = "/home/spil3141/Desktop/siteX/detector/static/detector/externals/Scaler_Model.sav"

    #Restoring Model
    loaded_model = tf.keras.models.load_model(loaded_model_path)
    loaded_model.load_weights(weights_path)
    loaded_stdsc = DataPreprocessing.Scale_with_loaded_sc(sc_path)

    def get_object(self):
        obj = super().get_object()
        #Converting img to numpy 1d array
        # img = spil.img_2_1d_arr(obj.image) -> Returns the path to the image of focus
        img_std = DataPreprocessing.flatten_2d_to_4d(DataPreprocessing.Scale_with_loaded_sc(DataPreprocessing.img_2_flatten_2d(obj.image),self.sc_path))

        #using the classifier to make prediction
        if self.clf:
            self.prediction = str(np.argmax(self.loaded_model.predict(img_std),axis = 1))
        else:
            self.prediction = "failed to load"

        return obj

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["prediction"] = self.prediction
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


