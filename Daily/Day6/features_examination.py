import pandas as pd
from sklearn.datasets import load_breast_cancer, load_diabetes, load_wine, load_iris
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression, LinearRegression
import numpy as n
from sklearn.metrics import accuracy_score
from sklearn import linear_model

#load data
data = load_breast_cancer()


#read data
X = data['data']
Y = data['target']
#preprocessing - extension
for sublst in X:
    for i, num in enumerate(sublst):
        sublst[i] = round(num, 1)


#choose model as LogisticRegression
model = LogisticRegression(penalty = "l2", solver = "newton-cholesky", fit_intercept = True, class_weight = 'balanced', multi_class = "ovr")
#solver = netwton-cholesky: This was the highest resulting accuracy. This solver is more efficient for larger datasets,
# requiring less memory and computational resources.
    #tried saga with elasticnet to mix both l1 and l2 penalties, but it ended with a .9 accuracy.
#fit_intercept = True: false brings it down by .002. A constant being added to the decision function helps the accuracy.
#class_weight = balanced: uses values of y, adjusting weights inversely proportion to class frequency
#multi_class = ovr: used for binary datasets 






#input X, Y into model
model.fit(X, Y)
#base Y value off X values
Y_predict = model.predict(X)

#print(Y)
#print(Y_predict)
#print(data.feature_names)

#print accuracy score
print(accuracy_score(Y, Y_predict))

#print(model.coef_)

#print weights with corresponding feature names
#for i in range(0,30):
    #print(data.feature_names[i])
    #print(model.coef_[0,i])

#plot weights on heatmap
#plt.imshow(model.coef_, aspect = 'auto')
#plt.colorbar()
#plt.show()


#This prints out the weight of every feature, whereas higher weights mean that
#the specific feature increased the chance of being positive by that many times.
#For example, mean radius contributed by making it .9 times more likely to be true.
