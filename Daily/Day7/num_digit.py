from skimage.io import imread
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#overall goal: come up with an X and Y that we can use to train a machine learning model
#to recognize digits


def process_images_and_labels(target):
    #read raw data and raw labels
    raw_images = []
    raw_labels = np.loadtxt('digits/'+target+'/_labels.csv')


    for i in range(1437):
        raw_images.append(imread("digits/"+target+"/"+str(i) +".png"))
    #convert the data to be the right format

    def basic_features(im):
        return im.reshape(64)

    feats = []

    for i in range(1437):
    #   take the ith raw image, put it into basic_features, reshae image, append to list of features
        feats.append(basic_features(raw_images[i]))

    #making an array out of a list
    X = np.array(feats)
    #list of labels
    labs = []

    #convert our labels to be the right format

    #loop over all rows of label matrix
    for i in range(len(raw_labels)):
        #get labels in ith row
        arr = raw_labels[i]
        #figure out which entry is turned to 1, add it to a list
        for j in range(10):
            if arr[j] == 1:
                labs.append(j)

    #make labs into array
    Y = np.array(labs)

    print(X, Y)



    #create our model
    model = LogisticRegression()


    #train our model
    model.fit(X,Y)
    #check the trained model's accuracy
    Y_predict = model.predict(X)
    print(accuracy_score(Y, Y_predict))

    return X,Y

trainX, trainY = process_images_and_labels("train")
testX, testY = process_images_and_labels("test")
