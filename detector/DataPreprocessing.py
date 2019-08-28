# -*- coding: utf-8 -*-

import PIL
from PIL import Image
import numpy
import numpy as np
import pandas as pd
import os
# import cv2

#Directory to Udemy Course Template file
BASE_DIR = "/Users/spil3141/Desktop/Machine Learning/Documentation/Machine Learning A-Z Template Folder"


def img_2_flatten_2d(filename):
  size = (28,28)
  img = Image.open(filename)
  img = img.resize(size,PIL.Image.ANTIALIAS)
  img = np.asarray(img)
  img = img[:,:,0]
  img = img.reshape(-1)
  img = img.reshape(-1,784)
  return img

from sklearn.externals import joblib

def Scale_with_loaded_sc(img_numpy_flatten_2d,model_path):
  loaded_scaler = joblib.load(model_path)
  img_std = stdsc.transform(img)
  return img_std

def flatten_2d_to_4d(arr):
  return arr.reshape((-1,28,28,1))


def from_img_to_1d(img):
    """from PIL import Image
    from skimage import color
    from skimage import io
    from skimage.transform import resize
    #Read and convert image to Grayscale
    img = color.rgb2gray(io.imread(img))
    #Resize image to a shape of (28,28)
    img = resize(img, (28,28),anti_aliasing=True)"""
    from PIL import Image
    img = Image.open(img)
    img = img.resize((28,28), Image.ANTIALIAS)
    img = numpy.asarray(img)
    img = img.reshape(-1)
    return img

#Resizing Images to 500x400
def resize():
    print("Resizing initiated!")
    #spil3141 Algorithm
    for top_dir in os.listdir(os.path.join(BASE_DIR,"Datasets")):
        if top_dir == "Orange":
            imgs_dir = os.path.join(BASE_DIR,"Datasets/"+ top_dir + "/Images/raw_images")
            for img in os.listdir(imgs_dir):
                if (img.endswith(".jpg")):
                    try:
                        pic = Image.open(os.path.join(imgs_dir,img))
                        pic = pic.resize((500, 400), PIL.Image.ANTIALIAS)
                        pic.save(os.path.join(imgs_dir,img))
                    except:
                        print("Error occured at file %s !" % (img))
    print("Resizing Completed!")



#Converting Image to Numpy array
def img_2_1d_arr(img):
    imgdata = Image.open(img)
    imgdata = imgdata.resize((8, 8), PIL.Image.ANTIALIAS)
    #imgdata.save(img)
    array = numpy.array(imgdata)
    if (array.ndim == 3):
        a = array[:,:,0]
        b = a.reshape(-1)
    elif (array.ndim == 2):
        b = array.reshape(-1)
    return b


# Converting Images to CSV Format
def img2csv():
    X = numpy.empty((200000,))
    X = numpy.insert(X,0,22)
    Y = 22

    print("Conversion Started !")
    for top_dir in os.listdir(os.path.join(BASE_DIR,"Datasets")):

        if top_dir == "Apple":
            print("setting up Dataset for Apple")
            img_dir = os.path.join(BASE_DIR,"Datasets/"+ top_dir + "/Images/raw_images")
            Y = 0
            for img in os.listdir(img_dir):
                if img.endswith(".jpg"):
                    imgdata = Image.open(os.path.join(img_dir,img))
                    array = numpy.array(imgdata)
                    a = array[:,:,0]
                    b = a.reshape(-1)
                    b = numpy.insert(b,0,Y)
                    X = numpy.vstack((X,b))
            print("Completed")

        if top_dir== "Orange":
            print("setting up Dataset for Orange")
            img_dir = os.path.join(BASE_DIR,"Datasets/"+ top_dir + "/Images/raw_images")
            Y = 1
            for img in os.listdir(img_dir):
                if img.endswith(".jpg"):
                    imgdata = Image.open(os.path.join(img_dir,img))
                    array = numpy.array(imgdata)
                    a = array[:,:,0]
                    b = a.reshape(-1)
                    b = numpy.insert(b,0,Y)
                    X = numpy.vstack((X,b))
            print("Compelted")

    #Saving Datasets to csv file
    print("Saving array to csv file")
    numpy.savetxt('Dataset.csv', X, delimiter=',',fmt="%.2f")
    print("Compelted")

    print("Conversion Completed !")




# Determine the labels and save it within a file .
def labelsetup():
    print("Labeling Started !")
    Y = list()
    for filename in os.listdir(BASE_DIR):
        if filename == "train_labels.csv":
            label_file_dir = os.path.join(BASE_DIR,filename)
            image_file_dir = os.path.join(BASE_DIR,"train")
            label_list = pd.read_csv(label_file_dir)
            for image_name in os.listdir(image_file_dir):
                if image_name.endswith(".JPG"):
                    for item in label_list.values:
                        if item[0].endswith(".JPG"):
                            if image_name == item[0]:
                                Y.append(item[3])
                                break;
    Dataset = numpy.asarray(Y)
    numpy.savetxt("Train_Labels.csv",Dataset,fmt="%s")
    print("Labeling Completed!")
