import numpy as np
import pandas as pd


# read data using pandas read_csv without headers
data = pd.read_csv('data_multi.csv', header=None)

# create the feature matrix X and the values matrix Y
X = data.values[:, :-1]
Y = data.values[:, -1][:, np.newaxis]
m = len(X)

# add  a column of ones at the start of the X matrix
X = np.hstack((np.ones((m, 1)), X))

# apply feature scaling on the feature matrix
for i in range(len(X[0])):
    column_vector = X[:, i]
    std = np.std(column_vector)
    if std == 0:
        continue
    avg = np.average(column_vector)
    X[:, i] = (column_vector - avg) / std


# initialize values for gradient descent parameters: alpha, iterations, theta predictions,
# number of training set examples

alpha = 0.1
iterations = 1000
theta = np.full((len(X[0]), 1), 0)

# write the loop to determine theta values using the matrix calculations
X_transposed = X.T
for i in range(0, iterations):
    hypothesis = np.dot(X, theta)
    loss = hypothesis - Y
    vectorized_gradient = np.dot(X_transposed, loss) / m
    theta = theta - alpha * vectorized_gradient

print(theta)
cost_theta = sum(np.power(X.dot(theta) - Y, 2) / m)
print("Cost of theta: ", cost_theta)

# write the normal equation
theta_normal = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)
print(theta_normal)
cost_theta_normal = sum(np.power(X.dot(theta_normal) - Y, 2) / m)
print("Cost of theta normal: ", cost_theta_normal)

print(f"Theta normal is {((cost_theta - cost_theta_normal) / cost_theta_normal) * 100}% better than theta")

