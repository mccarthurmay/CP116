import numpy as np
import matplotlib.pyplot as plt

#importing the model
from sklearn.linear_model import LinearRegression

# X is our model's input.
X = np.random.random(size=(10,1))

# Y is a linear function of X
Y = .4 * X   +  3.455
Y += 0.05*np.random.random(size=Y.shape)

#creating a new linear regression model
model = LinearRegression()

# fit the model to our data
model.fit(X,Y)

Y_pred = model.predict(X)

# plotting X vs Y
plt.scatter(X,Y)
plt.scatter(X,Y_pred)
plt.show()
