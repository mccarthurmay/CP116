#imports
from skimage.io import imread
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from PIL import Image, ImageFilter
import cv2
from skimage.filters import sobel
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.kernel_ridge import KernelRidge

def process_images_and_labels(target):

    #read the raw data and raw labels
    raw_labels = np.loadtxt(target + "_labels.csv")

    #kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])  #sharpening
    raw_images = []

    #go through every image and preprocess them
    for i in range(len(raw_labels)):
        #read ith image
        img = cv2.imread(target + "/" + str(i).zfill(4) + ".png")
        #resize img
        img = cv2.resize(img, (14, 22))

        #grayscale using opencv
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #GaussianBlur
        img = cv2.GaussianBlur(img, (3,3), 0)

        #add to list
        raw_images.append(img)

    #reshape image file
    def basic_features(im):
        return im.reshape(308)

    features = []

    #for every image, reshape
    for i in range(len(raw_labels)):
        features.append(basic_features(raw_images[i]))

    X = np.array(features)

    Y = raw_labels.astype(int)

    return X, Y

trainX, trainY = process_images_and_labels("mnist_train")
testX, testY = process_images_and_labels("mnist_valid")

model = LogisticRegression()
#model = MLPClassifier(hidden_layer_sizes=(1000), activation = "logistic", solver = "adam", learning_rate = "invscaling", )
#hls = 1000, layer of 1000 neurons that have weights for each number 0-9. (default of 2 layers)
#activation = logistic, activation function for the hidden layer, acts like a logistic regression with multiple layers
#solver = adam, default value... lbfgs works better with smaller datasets
#learning_rate = "invscaling" gradually decreases learning rate at each time step
#shuffler = "false"
model.fit(trainX, trainY)

Y_pred = model.predict(testX)
print(Y_pred[:5])
print(testY[:5])
print(accuracy_score(testY, Y_pred))
