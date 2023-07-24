# https://en.wikipedia.org/wiki/Gradient_descent
import numpy as np
import random

random.seed(42)

def gradient_descent(x, y, theta, alpha, m, num_iterations):
    """Gradient descent algorithm

    x (numpy.ndarray)       : input data
    y (numpy.ndarray)       : target variable
    theta (numpy.ndarray)   : parameters
    alpha (float)           : learning rate
    m (int)                 : number of examples
    num_iterations (int)    : number of iterations
    """
    x_transpose = x.transpose()

    for i in range(0, num_iterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        cost = np.sum(loss ** 2) / (2 * m)
        # print
        print("Iteration: %d, Cost: %f" % (i, cost))
        # average gradient per example
        gradient = np.dot(x_transpose, loss) / m
        # update
        theta = theta - alpha * gradient
    
    return theta

def generate_data(num_points, bias, variance):
    """Generate data

    num_points (int)    : number of points
    bias (int)          : bias
    variance (int)      : variance
    """
    x = np.zeros(shape=(num_points, 2))
    y = np.zeros(shape=num_points)
    # straight line
    for i in range(0, num_points):
        # bias feature
        x[i][0] = 1
        x[i][1] = 1
        # target variable
        y[i] = (i + bias) + random.uniform(0, 1) * variance
        
    return x, y

x, y = generate_data(100, 25, 10)
m, n = np.shape(x)
num_iterations = 10000
alpha = 0.0005
theta = np.ones(n)
theta = gradient_descent(x, y, theta, alpha, m, num_iterations)

# print
print(theta)

# Iteration: 0, Cost: 3417.449751
# Iteration: 1, Cost: 3411.478114
# Iteration: 2, Cost: 3405.518415
# ...
# Iteration: 9997, Cost: 430.137723
# Iteration: 9998, Cost: 430.137723
# Iteration: 9999, Cost: 430.137723
# [39.64610036 39.64610036]