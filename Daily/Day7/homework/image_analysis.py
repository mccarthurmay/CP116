#imports
from skimage.io import imread
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from PIL import Image, ImageFilter
import cv2
from skimage.filters import sobel


def process_images_and_labels(target):

    #read the raw data and raw labels
    raw_labels = np.loadtxt(target + "_labels.csv")

    #kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    raw_images = []
    for i in range(len(raw_labels)):

        img = cv2.imread(target + "/" + str(i).zfill(4) + ".png")
        img = cv2.resize(img, (14, 22)) #resize
        #img = cv2.normalize(img, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F) #normalization
        #img = cv2.filter2D(img, -1, kernel) #sharpening
        #img = cv2.Laplacian(img, cv2.CV_64F) #sharpening v2

        #cv2.imshow('edge', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        #raw_images.append(np.array(Image.open(target + "/" + str(i).zfill(4) + ".png").convert('L'))) #grayscale with Pillow module
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale
        img = cv2.GaussianBlur(img, (3,3), 0) #Gaussian Blur
        raw_images.append(img) #add to list
        #try corners
    def basic_features(im):
        return im.reshape(308)#308   #784 #choose different features - like im.max)_ im. mean(), im[4,4]

    features = []

    for i in range(len(raw_labels)):
        features.append(basic_features(raw_images[i]))

    X = np.array(features)


    Y = raw_labels.astype(int)

    return X, Y


trainX, trainY = process_images_and_labels("mnist_train")
testX, testY = process_images_and_labels("mnist_valid")

model = LogisticRegression() #try neural net
model.fit(trainX, trainY)

Y_pred = model.predict(testX)
print(Y_pred[:5])
print(testY[:5])
print(accuracy_score(testY, Y_pred))

#FLATTENING IMAGE
#used image flattening + logistic regression - .8795
#used image flattening grayscaled (used Pillow module) + logistic regression = 0.8795
#used image flattening, grayscaled, then applied gaussian blur (opencv) + logistic regression = .8865 !!!
#tried opencv edge detection - .7925
#conclusion:
    #flattened, grayscaled (opencv), gaussian blur (opencv), resize + logisitcal regression = .9105!!
#

#normalization https://www.tutorialspoint.com/how-to-normalize-an-image-in-opencv-python
