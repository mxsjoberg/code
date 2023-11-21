# https://en.wikipedia.org/wiki/Gradient_descent
import numpy as np
import random

# 1. calculate hypothesis h = X * theta
# 2. calculate loss = h - y, squared cost = (loss ** 2) / (2 * m)
# 3. calculate gradient = X' * loss / m
# 4. update parameters thete = theta - alpha * gradient
#
# m: number of examples

def gradient_descent(x, y, theta, alpha, m, num_iterations):
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

# generate points with bias, variance (noise)
x, y = generate_data(100, 25, 10)
m, n = np.shape(x)
num_iterations = 10000
alpha = 0.0005
theta = np.ones(n)
theta = gradient_descent(x, y, theta, alpha, m, num_iterations)

# print
print(theta)

# Iteration: 0, Cost: 3440.881818
# Iteration: 1, Cost: 3434.861831
# .
# .
# .
# Iteration: 9998, Cost: 429.382775
# Iteration: 9999, Cost: 429.382775
# [39.80223561 39.80223561]