import tensorflow as tf
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
import platform
from . import models
from . import forms
import numpy as np
import joblib
from . import DataPreprocessing
from django.views.generic import (CreateView,
                                  DetailView,
                                  ListView,
                                  TemplateView
                                  )
# /Users/spil3141/Desktop/siteX/detector/static/detector/externals/digits_model_full.sav

# Desktop/siteX/detector/static/detector/externals/digits_model_full.sav


class Success(DetailView):
    model = models.Item
    loaded_model = None
    # Assigning Absolute path based on OS
    if (platform.system() == "Linux"):
        loaded_model_path = "/home/spil3141/siteX/detector/static/detector/externals/Saved_Model_20190910-124505"
        # weights_path = "/home/spil3141/Desktop/siteX/detector/static/detector/externals/cnn_checkpoint.h5"
        sc_path = "/home/spil3141/siteX/detector/static/detector/externals/Scaler_Model.sav"
        #Restoring Model
        # loaded_model = tf.keras.models.load_model(loaded_model_path)
        # loaded_model.load_weights(weights_path)
        loaded_model = tf.keras.experimental.load_from_saved_model(loaded_model_path)
        loaded_model.compile(loss = "categorical_crossentropy",
                     optimizer = "adam",
                     metrics = ["acc"])
    else:
        loaded_model_path = "C:/Users/Changun/Desktop/spil's stuff/Projects/siteX/detector/static/detector/externals/Saved_Model_20190910-124505"
        # weights_path = "C:/Users/Changun/Desktop/spil's stuff/Projects/siteX/detector/static/detector/externals/cnn_checkpoint.h5"
        sc_path = "C:/Users/Changun/Desktop/spil's stuff/Projects/siteX/detector/static/detector/externals/Scaler_Model.sav"
        #Restoring Model
        loaded_model = tf.keras.models.load_model(loaded_model_path)
        # loaded_model.load_weights(weights_path)
        # loaded_model = tf.keras.experimental.load_from_saved_model(loaded_model_path)
        # loaded_model.compile(loss = "categorical_crossentropy",
        #              optimizer = "adam",
        #              metrics = ["acc"])
    def get_object(self):
        obj = super().get_object()
        #Converting img to numpy 1d array
        # img = spil.img_2_1d_arr(obj.image) -> Returns the path to the image of focus

        #using the classifier to make prediction
        if self.loaded_model != None:
            img_std = DataPreprocessing.flatten_2d_to_4d(DataPreprocessing.Scale_with_loaded_sc(DataPreprocessing.img_2_flatten_2d(obj.image),self.sc_path))
            # self.prediction = str(np.argmax(self.loaded_model.predict(img_std),axis = 1))
            # self.probability = str("%.3f Percent" % (np.amax(self.loaded_model.predict(img_std)) * 100))
            self.prediction = str(img_std.shape)
            self.probability = "Error"
            print(self.loaded_model.predict_classes(img_std.reshape((1,28,28,1))))
        else:
            self.prediction = "Error"
            self.probability = "Error"
        return obj

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["prediction"] = self.prediction
        context["probability"] = self.probability
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
