import random
import numpy as np
import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


def normalize(x):
    return x * (np.max(x, axis=0) ** -1)


def read_libsvm(file):
    data = open(file).read().split('\n')
    observations = [data[i].split() for i in range(len(data))]
    y = []
    x = []
    for obs in observations:
        y.append(float(obs[0]))
        x.append([1.0, float(obs[1].split(':')[1]), float(obs[2].split(':')[1])])
    return x, y


def logistic(x, w):
    return 1 / (1 + np.exp(-(x @ w)))


def preceptron(x, y, alpha, w):
    index = list(range(len(x)))
    for epoch in range(1, 500):
        random.shuffle(index)
        for i in index:
            logi = logistic(x[i, :], w)
            w = w + alpha * ((y[i] - logi) * logi * (1 - logi) * x[i, :])

    return w


x, y = read_libsvm('salammbo_a.libsvm')
y = np.array(y)
x = normalize(np.array(x))

w = np.ones((3))
alpha = 0.6

w = preceptron(x, y, alpha, w)
print(w)
plt.plot(x[0:15, 1], x[0:15, 2], 'b.')
plt.plot(x[15:30, 1], x[15:30, 2], 'r.')
plt.plot([0, 1], [w[0]/(-w[2]), (w[0] + w[1])/(-w[2])])
plt.show()
