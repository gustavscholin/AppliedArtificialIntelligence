#
# Perform the linear regression for the number of characters vs numbers of a's in the text
# Author: Noah Solomon, Gustav Scholin
#


import lab3.datasets as ds
import copy
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


# ----------------
# Helper Functions
# ----------------


# Normalize a list by its largest value
# Parameters: List to normalize
# Return: Normalized list
def normalize_data(in_list):
    max_val = in_list[0]
    for i in range(0, len(in_list)):
        if max_val < in_list[i]:
            max_val = in_list[i]
    ret_list = copy.deepcopy(in_list)
    for i in range(0, len(ret_list)):
        ret_list[i] = ret_list[i] / max_val
    return ret_list


# Function to find the best fit line using batch gradient descent
# Parameters: list of chars, list of as, and learning rate
# Return: Weights w0 and w1 in the line y = w0 + w1*x
def fit_line_batch(char_list, a_list, rate):
    w0, w1 = 0.5, 0.5

    # Start gradient descent
    for i in range(0, 500):
        w0_loss = 0
        w1_loss = 0

        # Calculate the loss for w0 and w1
        for j in range(0, len(a_list)):
            w0_loss = w0_loss + (char_list[j] - (w0 + w1 * a_list[j]))
            w1_loss = w1_loss + (char_list[j] - (w0 + w1 * a_list[j])) * a_list[j]

        print((w0_loss, w1_loss))
        w0 = w0 + rate * w0_loss
        w1 = w1 + rate * w1_loss

    return w0, w1


def fit_line_batch_vec(char_list, a_list, rate, w):
    pass


# Function to find the best fit line using stochastic gradient descent
# Parameters: number of total characters, number of as, and learning rate
# Return: Weights w0 and w1 in the line y = w0 + w1*x
def fit_line_stochastic(char_list, a_list, rate):
    w0, w1 = 0.5, 0.5
    return w0, w1


# ------------------------------
# Linear Regression Script Start
# ------------------------------

# Retrieve data
en_chars, en_as = ds.get_data_en()
fr_chars, fr_as = ds.get_data_fr()

# Normalize data to range [0,1]
en_chars_n = normalize_data(en_chars)
en_as_n = normalize_data(en_as)
fr_chars_n = normalize_data(fr_chars)
fr_as_n = normalize_data(fr_as)

l_rate = 0.1  # Learning rate for the gradient descent

# Calculate batch linear regression
en_w0, en_w1 = fit_line_batch(en_chars_n, en_as_n, l_rate)
fr_w0, fr_w1 = fit_line_batch(fr_chars_n, fr_as_n, l_rate)

print((en_chars_n, en_as_n))

plt.plot(en_chars_n, en_as_n, '.')
plt.plot([0, 1], [en_w0, en_w1 + en_w0])
plt.show()
