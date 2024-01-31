#imports
from skimage.io import imread
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd



    #read the raw data and raw labels
valid_labels = np.loadtxt("mnist_valid_labels.csv")
print(valid_labels)

valid_images = []
for i in range(len(valid_labels)):
    valid_images.append(imread("mnist_valid/"+str(i).zfill(4)+".png"))

def basic_features(im):
    return im.reshape(784)

features = []

for i in range(len(valid_labels)):
    features.append(basic_features(valid_images[i]))

X = np.array(features)
print(valid_labels[:10])


Y = valid_labels.astype(int)

np.set_printoptions(threshold=np.inf)


print (X, Y)
