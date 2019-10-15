from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
import platform
from . import models
from . import forms
import numpy as np
# import tensorflow as tf
from . import DataPreprocessing
from django.views.generic import (CreateView,
                                  DetailView,
                                  ListView,
                                  TemplateView
                                  )

# def predi(img_path):
#     if (platform.system() == "Linux"):
#         loaded_model = tf.keras.models.load_model("/home/spil3141/siteX/detector/static/detector/externals/Saved_Model.h5")
#         scaler_model_path = "/home/spil3141/siteX/detector/static/detector/externals/Scaler_Model.sav"
#     elif platform.system() == "Windows":
#         loaded_model = tf.keras.models.load_model('C:/Users/spil3141/Desktop/siteX/detector/static/detector/externals/Saved_Model.h5')
#         scaler_model_path = "C:/Users/spil3141/Desktop/siteX/detector/static/detector/externals/Scaler_Model.sav"
#     sample = DataPreprocessing.preprocess(img_path,scaler_model_path)
#     prediction = str(loaded_model.predict_classes(sample))
#     return prediction, str("%.1f Percent" % (np.amax(loaded_model.predict(sample)) * 100))

class Success(DetailView):
    model = models.Item
    loaded_model = None
    # Assigning Absolute path based on OS
    # if (platform.system() == "Linux"):
    #     loaded_model = tf.keras.models.load_model("/home/spil3141/siteX/detector/static/detector/externals/Saved_Model.h5")
    #     scaler_model_path = "/home/spil3141/siteX/detector/static/detector/externals/Scaler_Model.sav"
    # elif platform.system() == "Windows":
    #     new_model = tf.keras.models.load_model('C:/Users/spil3141/Desktop/Testing_TF/app/static/app/externals/Saved_Model.h5')
    #     scaler_model_path = "C:/Users/spil3141/Desktop/Testing_TF/app/static/app/externals/Scaler_Model.sav"
    #     img_path = "C:/Users/spil3141/Desktop/Testing_TF/app/static/app/images/img.png"


    def get_object(self):
        obj = super().get_object() #Converting img to numpy 1d array :  img_path == obj.image -> Returns the path to the image of focus
        # self.prediction, self.probability = predi(obj.image)
        self.prediction, self.probability = "Error","Error"
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
# sample = DataPreprocessing.preprocess(self.img_path,self.scaler_model_path)
# prediction = str(self.new_model.predict_classes(sample))
#the classifier to make prediction
# if self.loaded_model != None:
#     self.prediction, self.probability = predi(obj.image)
#     # img_std = DataPreprocessing.preprocess(obj.image,self.scaler_model_path)
#     # self.probability = str("%.3f Percent" % (np.amax(self.loaded_model.predict(img_std)) * 100))
#     # self.prediction = str(self.loaded_model.predict_classes(sample))
#     # try:
#     #     img_std = DataPreprocessing.preprocess(obj.image,scaler_model_path)
#     #     self.probability = str("%.3f Percent" % (np.amax(self.loaded_model.predict(img_std)) * 100))
#     #     self.prediction = str(self.loaded_model.predict_classes(sample))
#     # except:
#     #     self.prediction = "Error while preprocessing and predicting "
#     #     self.probability = "Error while preprocessing and predicting "
# else:
#     self.prediction = Error
#     self.probability = "Error"
