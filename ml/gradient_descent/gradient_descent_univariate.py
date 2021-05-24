import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def read_training_set():
    data = pd.read_csv('data.csv', header=None)
    return data.iloc[:, 0], data.iloc[:, 1]


X, y = read_training_set()

# initialize gradient descent
m = len(X)
iterations = 1000
alpha = 0.0001
theta1 = 0
theta2 = 0

# implement gradient descent
for i in range(iterations):
    predicted_value = theta1 + X * theta2

    tempTheta1 = theta1 - alpha * (1 / m) * sum(predicted_value - y)
    tempTheta2 = theta2 - alpha * (1 / m) * sum((predicted_value - y) * X)

    theta1 = tempTheta1
    theta2 = tempTheta2

predicted_value = theta1 + X * theta2

plt.scatter(X, y)
plt.plot(X, predicted_value, color='red')
plt.show()
