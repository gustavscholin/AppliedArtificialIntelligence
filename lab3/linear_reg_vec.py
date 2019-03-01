import random
import numpy as np
import lab3.datasets as ds
import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


def normalize(vec):
    maximum = np.max(vec)
    D = np.diag(maximum * np.ones(vec.size))
    vec = vec @ np.linalg.inv(D)
    return vec


def batch_gradient_decent(x, y, alpha, w):
    for epoch in range(1, 500):
        w_old = w
        loss = y - w @ x
        gradient = loss @ x.T
        w = w_old + alpha * gradient

        if np.linalg.norm(w - w_old) / np.linalg.norm(w) < 0.0005:
            print("Epoch", epoch)
            break
    return w


def stoch_grad_decent(x, y, alpha, w):
    for epoch in range(1, 500):
        index = list(range(x.shape[1]))
        random.shuffle(index)
        for i in index:
            w_old = w
            loss = y[0, i] - w @ x[:, i]
            gradient = loss * x[:, i]
            w = w_old + alpha * gradient

        if np.linalg.norm(w - w_old) / np.linalg.norm(w) < 0.0005:
            print("Epoch", epoch)
            break
    return w


x_en, y_en = ds.get_data_en()
x_fr, y_fr = ds.get_data_fr()

x_en = normalize(np.array(x_en))
y_en = normalize(np.array([y_en]))

x_fr = normalize(np.array(x_fr))
y_fr = normalize(np.array([y_fr]))

x_en = np.concatenate((x_en, np.ones(x_en.size))).reshape(2, x_en.size)
x_fr = np.concatenate((x_fr, np.ones(x_fr.size))).reshape(2, x_fr.size)

w = np.ones((1, 2))
alpha = 0.1

w_en_batch = batch_gradient_decent(x_en, y_en, alpha, w)
w_fr_batch = batch_gradient_decent(x_fr, y_fr, alpha, w)

plt.plot(x_en[0,:], y_en[0,:], '.')
plt.plot([0, 1], [w_en_batch[0, 1], w_en_batch[0, 1] + w_en_batch[0, 0]])

plt.plot(x_fr[0,:], y_fr[0,:], '.')
plt.plot([0, 1], [w_fr_batch[0, 1], w_fr_batch[0, 1] + w_fr_batch[0, 0]])

plt.title('Linear Regression, Batch Gradient Decent')

w_en_stoch = stoch_grad_decent(x_en, y_en, alpha, w)
w_fr_stoch = stoch_grad_decent(x_fr, y_fr, alpha, w)

plt.figure()
plt.plot(x_en[0, :], y_en[0, :], '.')
plt.plot([0, 1], [w_en_stoch[0, 1], w_en_stoch[0, 1] + w_en_stoch[0, 0]])

plt.plot(x_fr[0, :], y_fr[0, :], '.')
plt.plot([0, 1], [w_fr_stoch[0, 1], w_fr_stoch[0, 1] + w_fr_stoch[0, 0]])

plt.title('Linear Regression, Stochastic Gradient Decent')
plt.show()
