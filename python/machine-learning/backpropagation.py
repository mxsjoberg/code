# Backpropagation is a method used in artificial neural
# networks to calculate a gradient that is needed in the
# calculation of the weights to be used in the network. 

# https://en.wikipedia.org/wiki/Backpropagation

import numpy as np

np.random.seed(42)

# https://en.wikipedia.org/wiki/Sigmoid_function
def sigmoid(x): return 1.0 / (1 + np.exp(-x))

assert(sigmoid(0) == 0.5)

# derivative of sigmoid
def sigmoid_dx(x): return x * (1.0 - x)

assert(sigmoid_dx(0.5) == 0.25)

# input
x = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]])
y = np.array([[0], [1], [1], [0]])
# weights
w_1 = np.random.rand(x.shape[1],4)
w_2 = np.random.rand(4,1)
# output
output = np.zeros(y.shape)

def feedforward(x, w_1, w_2, output):
    layer_1 = sigmoid(np.dot(x, w_1))
    output = sigmoid(np.dot(layer_1, w_2))

    return layer_1, w_1, w_2, output

def backpropagation(layer_1, w_1, w_2, x, y, output):
    w_2_dx = np.dot(
        np.transpose(layer_1),
        (2 * (y - output) * sigmoid_dx(output))
    )
    w_1_dx = np.dot(
        np.transpose(x),
        (np.dot(2 * (y - output) * sigmoid_dx(output), np.transpose(w_2)) * sigmoid_dx(layer_1))
    )
    # update weights
    w_1 += w_1_dx
    w_2 += w_2_dx

    return layer_1, w_1, w_2, x, y, output

# run
for i in range(1500):
    layer_1, w_1, w_2, output = feedforward(x, w_1, w_2, output)
    layer_1, w_1, w_2, x, y, output = backpropagation(layer_1, w_1, w_2, x, y, output)

print(output)
# [[0.01043733]
#  [0.97230567]
#  [0.97090151]
#  [0.03501066]]