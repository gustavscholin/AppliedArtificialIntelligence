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
    return x * np.max(x, axis=0) ** -1


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


# The threshold function.
# Parameters: Vector of one observation x and a weight vector w
# Return: 1 if the dot product between x and w is >= 0, otherwise 0
def threshold(x, w):
    if (x @ w) >= 0:
        return 1
    else:
        return 0


# Function to update the weight vector according to the perceptron learning rule.
# Parameters: Observations matrix x, class vector y, learning rate alpha
# and weight vector w
# Return: The updated weight vector
def preceptron(x, y, alpha, w):
    tol = 0
    index = list(range(len(x)))
    # Start the perceptron learning
    for epoch in range(1, 500):
        mis_class = 0
        # Randomize the order of the observations
        random.shuffle(index)
        for i in index:
            clas = y[i] - threshold(x[i, :], w)
            w = w + alpha * clas * x[i, :]
            # Count misclassifications
            mis_class += abs(clas)

        # Breaks if the misclassified observations is lower or equals to
        # to the tolerance level
        if mis_class <= tol:
            print("Epoch", epoch)
            break
    return w


# --------------------------------------
# Perceptron Classification Script Start
# --------------------------------------

# Read and normalize observations matrix and class vector
x, y = read_libsvm('salammbo_a.libsvm')
y = np.array(y)
x = normalize(np.array(x))

# Define initial weight vector and learning rate
w = np.ones((3))
alpha = 0.1

# Train the weights
w = preceptron(x, y, alpha, w)

print(w)

# Plot the result
plt.plot(x[0:15, 1], x[0:15, 2], 'b.')
plt.plot(x[15:30, 1], x[15:30, 2], 'r.')
plt.plot([0, 1], [w[0] / (-w[2]), (w[0] + w[1]) / (-w[2])])
plt.title('Linear Classification, Perceptron')
plt.show()
