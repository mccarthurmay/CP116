# Overall goal: come up with an X and Y that we can
# use to train a machine learning model to recognize digits.
# imports
from skimage.io import imread
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def process_images_and_labels(target):
    # Read in the raw data and raw labels
    # --- Read in the images

    # --- Read in the labels
    raw_labels = np.loadtxt(target+"_labels.csv")
    print(raw_labels)

    raw_images = []
    for i in range(len(raw_labels)):
        raw_images.append(imread(target+"/"+str(i)+".png"))

    for i in range(10):
        print(raw_images[i])



    # Convert the data to be the right format.

    def basic_features(im):
        return im.reshape(64)

    feats = []

    for i in range(len(raw_labels)):
        feats.append(basic_features(raw_images[i]))


    X = np.array(feats)
    print(X.shape)

    # Convert our labels to be the right format.
    labs = []

    # loop over all the rows of our label matrix
    for i in range(len(raw_labels)):
        # get the labels in the ith row
        arr = raw_labels[i]
        # figure out which entry is turned to 1,
        # and add that index to our list of labels.
        for j in range(10):
            if arr[j] == 1:
                labs.append(j)

    Y = np.array(labs)

    print(X, Y)

    return X,Y



trainX, trainY = process_images_and_labels("train")
testX, testY = process_images_and_labels("test")









# Create our model.
model = LogisticRegression()


# Train our model.
model.fit(trainX,trainY)



# Check the trained model's accuracy.
Y_pred = model.predict(testX)
print(Y_pred[:20])
print(testY[:20])
print(accuracy_score(testY, Y_pred))
