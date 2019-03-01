import random
import numpy as np
import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


# ----------------
# Helper Functions
# ----------------

# Function to normalize the observations matrix
# Parameters: Matrix to normalize
# Return: Normalized matrix
def normalize(x):
    return x * (np.max(x, axis=0) ** -1)


# Function to read a observations matrix (x) and a vector of the
# corresponding true classes (y).
# Parameters: libsvm file
# Return: Observations matrix x and class vector y
def read_libsvm(file):
    data = open(file).read().split('\n')
    observations = [data[i].split() for i in range(len(data))]
    y = []
    x = []
    for obs in observations:
        y.append(float(obs[0]))
        x.append([1.0, float(obs[1].split(':')[1]), float(obs[2].split(':')[1])])
    return x, y

# The logistic function.
# Parameters: Vector of one observation x and a weight vector w
# Return: The value for the logistic function for the dot product between x and w
def logistic(x, w):
    return 1 / (1 + np.exp(-(x @ w)))


# Function to update the weight vector according to the update rule for logistic regression.
# Parameters: Observations matrix x, class vector y, learning rate alpha
# and weight vector w
# Return: The updated weight vector
def logistic_regression(x, y, alpha, w):
    index = list(range(len(x)))
    for epoch in range(1, 1000):
        random.shuffle(index)
        for i in index:
            logi = logistic(x[i, :], w)
            w = w + alpha * ((y[i] - logi) * logi * (1 - logi) * x[i, :])

    return w


# --------------------------------------
# Logistic Classification Script Start
# --------------------------------------

# Read and normalize observations matrix and class vector
x, y = read_libsvm('salammbo_a.libsvm')
y = np.array(y)
x = normalize(np.array(x))

# Define initial weight vector and learning rate
w = np.ones((3))
alpha = 0.6

# Train the weights
w = logistic_regression(x, y, alpha, w)

# Plot the result
plt.plot(x[0:15, 1], x[0:15, 2], 'b.')
plt.plot(x[15:30, 1], x[15:30, 2], 'r.')
plt.plot([0, 1], [w[0] / (-w[2]), (w[0] + w[1]) / (-w[2])])
plt.title('Linear Classification, Logistic Regression')
plt.show()
