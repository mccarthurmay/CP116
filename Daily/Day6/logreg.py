import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
import numpy as np
from sklearn.metrics import accuracy_score
# load the data

data = load_iris()




#unpack data
X = data["data"]
Y = data["target"]




model = LogisticRegression()
model.fit(X, Y)

Y_predict = model.predict(X)

print(Y)
print(Y_predict)
print(accuracy_score(Y, Y_predict))
