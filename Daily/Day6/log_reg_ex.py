from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
data = load_iris()
X = data["data"]
Y = data["target"]
print(X)
print(Y)

#X = np.random.random(size=(32,1))
#Y = X > .5
# convert Y to 0s and 1s
#Y = Y.astype('float')
#Y = Y.reshape(-1)

#creating a new linear regression model
model = LogisticRegression()

# fit the model to our data
model.fit(X,Y)

Y_pred = model.predict(X)

print(accuracy_score(Y,Y_pred))
print(model.coef_)
# plotting X vs Y
plt.scatter(X,Y)
plt.scatter(X,Y_pred)
plt.show()
