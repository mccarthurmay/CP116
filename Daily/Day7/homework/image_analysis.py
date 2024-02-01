#imports
from skimage.io import imread
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from PIL import Image, ImageFilter
import cv2
from skimage.filters import sobel
from sklearn.neural_network import MLPClassifier, MLPRegressor

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

        #normalize img
        #img = cv2.normalize(img, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)

        #sharpen img
        #img = cv2.filter2D(img, -1, kernel)

        #sharpen img
        #img = cv2.Laplacian(img, cv2.CV_64F)

        #test edge of image
        #cv2.imshow('edge', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        #grayscale using Pillow
        #raw_images.append(np.array(Image.open(target + "/" + str(i).zfill(4) + ".png").convert('L')))

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


#model = LogisticRegression()
#10 numbers - 10 hidden layers... what if we used 1000 hidden layers... * 3
model = MLPClassifier([1000,1000,1000])
model.fit(trainX, trainY)

Y_pred = model.predict(testX)
print(Y_pred[:5])
print(testY[:5])
print(accuracy_score(testY, Y_pred))

#Preprocessing

#used image flattening + logistic regression - .8795

#used image flattening grayscaled (used Pillow module) + logistic regression = 0.8795

#used image flattening, grayscaled (opencv), then applied gaussian blur (opencv) + logistic regression = .8865 !!!
    #opencv grayscale was likely stronger, gaussian blur smoothed edges that may confuse some numbers (some were low quality with weird edges)

#used opencv edge detection - .7925
    #many images had edges that were not clear, some 3s and 7s could be confused for 2s and 1s if the edges are smushed together

#used flattened, grayscaled (opencv), gaussian blur (opencv), resize + logisitcal regression = .9105!!
    #resize[14,22] stretched the image by its height, likely making the space between lines on numbers like 3, 2, 5, and 7 more prominent.

#MLPClassifier
#flattened image, grayscaled, gaussian blur, resize + MLPClassifier with 3 hidden layers (1000 nodes each) = .96!!!!!

#flattened image: allows a detailed reading of all rgb values of every image.

#grayscale: makes each image slightly more concrete. There would be less variation between the trained values.

#gaussian blur: takes away any harsh edges.

#resize[14,22]: allows for longer numbers to become more distinct. A 3 would look less like a 2, and a 7 would look less like a 1. [14,22] was chosen through trial and error

#MLPClassifier uses multiple hidden layers that contain neurons. Each layer of neurons captures complex patterns in the data. The more neurons, the more patterns can be found,
#but it also takes a lot longer. I believe that something could be "overfit", where some things may be overanalyzed and classified as something else. One layer of
#10,000 neurons did worse than one layer of 1,000 neurons. I received the highest accuracy with 3x1000 nodes, but 6x100 nodes is only .03% off for a much faster result.
