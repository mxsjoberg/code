# https://en.wikipedia.org/wiki/Delta_rule
import numpy as np
from prettytable import PrettyTable

# configuration variables
# -----------------------------------------------------------
# initial values
w = [1, 0, 0]

# learning rate
n = 1

# iterations
iterations = 12

# dataset
# -----------------------------------------------------------
X = [[1, 0, 2],
     [1, 1, 2],
     [1, 2, 1],
     [1, -3, 1],
     [1, -2, -1],
     [1, -3, -2]]

# classes
t = [1, 1, 1, 0, 0, 0]

# Heaviside function (https://en.wikipedia.org/wiki/Heaviside_step_function)
# -----------------------------------------------------------
def transfer_function(w, x):
    wx = np.dot(w, x)

    if (wx > 0):
        return 1
    elif (wx == 0):
        return 0.5
    else:
        return 0

assert (transfer_function([0.1, -0.5, 0.4], [0.1, -0.5, 0.4]) == 1)
assert (transfer_function([0.1, -0.5, 0.4], [0.1, 0.5, 0.4]) == 0)
assert (transfer_function([0, 0, 0], [0, 0, 0]) == 0.5)

# sequential delta learning algorithm
# -----------------------------------------------------------
result = []
for o in range(int(iterations / len(X))):
    for i in range(len(X)):
        if ((i + 1 + (len(X) * o)) > iterations): break

        w_prev = w
        x = X[i]
        y = transfer_function(w, x)

        # calculate update part
        update = np.zeros(len(x))
        for j in range(len(x)): update[j] = n * (t[i] - y) * x[j]

        # add update part to a
        w = np.add(w, update)

        # append result
        result.append((str(i + 1 + (len(X) * o)), np.round(w_prev, 4), np.round(x, 4), np.round(y, 4), np.round(t[i], 4), np.round(w, 4)))

# prettytable
# -----------------------------------------------------------
pt = PrettyTable(('iteration', 'w', 'x', 'y = H(wx)', 't', 'w_new'))
for row in result: pt.add_row(row)

pt.align['iteration'] = 'c'
pt.align['w'] = 'l'
pt.align['x'] = 'l'
pt.align['y = H(wx)'] = 'l'
pt.align['t'] = 'c'
pt.align['w_new'] = 'l'

print(pt)

# +-----------+---------------+------------+-----------+---+---------------+
# | iteration | w             | x          | y = H(wx) | t | w_new         |
# +-----------+---------------+------------+-----------+---+---------------+
# |     1     | [1 0 0]       | [1 0 2]    | 1         | 1 | [1. 0. 0.]    |
# |     2     | [1. 0. 0.]    | [1 1 2]    | 1         | 1 | [1. 0. 0.]    |
# |     3     | [1. 0. 0.]    | [1 2 1]    | 1         | 1 | [1. 0. 0.]    |
# |     4     | [1. 0. 0.]    | [ 1 -3  1] | 1         | 0 | [ 0.  3. -1.] |
# |     5     | [ 0.  3. -1.] | [ 1 -2 -1] | 0         | 0 | [ 0.  3. -1.] |
# |     6     | [ 0.  3. -1.] | [ 1 -3 -2] | 0         | 0 | [ 0.  3. -1.] |
# |     7     | [ 0.  3. -1.] | [1 0 2]    | 0         | 1 | [1. 3. 1.]    |
# |     8     | [1. 3. 1.]    | [1 1 2]    | 1         | 1 | [1. 3. 1.]    |
# |     9     | [1. 3. 1.]    | [1 2 1]    | 1         | 1 | [1. 3. 1.]    |
# |     10    | [1. 3. 1.]    | [ 1 -3  1] | 0         | 0 | [1. 3. 1.]    |
# |     11    | [1. 3. 1.]    | [ 1 -2 -1] | 0         | 0 | [1. 3. 1.]    |
# |     12    | [1. 3. 1.]    | [ 1 -3 -2] | 0         | 0 | [1. 3. 1.]    |
# +-----------+---------------+------------+-----------+---+---------------+

'''
Michael Sjoeberg
2020-04-10
https://github.com/michaelsjoeberg/python-playground/blob/master/machine-learning/delta-learning-algorithm.py
'''