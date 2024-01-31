import pandas as pd
from sklearn.datasets import load_breast_cancer, load_diabetes, load_wine, load_iris
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression, LinearRegression
import numpy as n
from sklearn.metrics import accuracy_score


#load data
data = load_breast_cancer()

#read data
X = data['data']
Y = data['target']

#choose model as LogisticRegression
model = LogisticRegression()
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
for i in range(0,30):
    print(data.feature_names[i])
    print(model.coef_[0,i])

#plot weights on heatmap
plt.imshow(model.coef_, aspect = 'auto')
plt.colorbar()
plt.show()

#This prints out the weight of every feature, whereas higher weights mean that
#the specific feature increased the chance of being positive by that many times.
#For example, mean radius contributed by making it .9 times more likely to be true.
