# https://www.cs.princeton.edu/courses/archive/spring13/cos511/scribe_notes/0411.pdf
import numpy as np
from prettytable import PrettyTable

# configuration variables
# -----------------------------------------------------------
# initial values
a = [1, 0, 0]

# margin vector
b = [1, 1, 1, 1, 1, 1]

# learning rate
n = 0.1

# iterations
iterations = 12

# dataset
# -----------------------------------------------------------
X = [[0, 2], [1, 2], [2, 1], [-3, 1], [-2, 1], [-3, 2]]
Y = [[1, 0, 2], [1, 1, 2], [1, 2, 1], [-1, 3, -1], [-1, 2, 1], [-1, 3, 2]]

# sequential widrow-hoff learning algorithm
# -----------------------------------------------------------
result = []
for o in range(int(iterations / len(Y))):
    for i in range(len(Y)):
        a_prev = a
        y = Y[i]

        # calculate ay
        ay = np.dot(a, y)

        # calculate update part
        update = np.zeros(len(y))
        for j in range(len(y)): update[j] = n * (b[i] - ay) * y[j]

        # add update part to a
        a = np.add(a, update)

        # append result
        result.append((str(i + 1 + (len(Y) * o)), np.round(a_prev, 4), np.round(y, 4), np.round(ay, 4), np.round(a, 4)))

# prettytable
# -----------------------------------------------------------
pt = PrettyTable(('iteration', 'a', 'y', 'ay', 'a_new'))
for row in result: pt.add_row(row)

pt.align['iteration'] = 'c'
pt.align['a'] = 'l'
pt.align['y'] = 'l'
pt.align['ay'] = 'l'
pt.align['a_new'] = 'l'

print(pt)

# +-----------+---------------------------+------------+--------+---------------------------+
# | iteration | a                         | y          | ay     | a_new                     |
# +-----------+---------------------------+------------+--------+---------------------------+
# |     1     | [1 0 0]                   | [1 0 2]    | 1      | [1. 0. 0.]                |
# |     2     | [1. 0. 0.]                | [1 1 2]    | 1.0    | [1. 0. 0.]                |
# |     3     | [1. 0. 0.]                | [1 2 1]    | 1.0    | [1. 0. 0.]                |
# |     4     | [1. 0. 0.]                | [-1  3 -1] | -1.0   | [ 0.8  0.6 -0.2]          |
# |     5     | [ 0.8  0.6 -0.2]          | [-1  2  1] | 0.2    | [ 0.72  0.76 -0.12]       |
# |     6     | [ 0.72  0.76 -0.12]       | [-1  3  2] | 1.32   | [ 0.752  0.664 -0.184]    |
# |     7     | [ 0.752  0.664 -0.184]    | [1 0 2]    | 0.384  | [ 0.8136  0.664  -0.0608] |
# |     8     | [ 0.8136  0.664  -0.0608] | [1 1 2]    | 1.356  | [ 0.778   0.6284 -0.132 ] |
# |     9     | [ 0.778   0.6284 -0.132 ] | [1 2 1]    | 1.9028 | [ 0.6877  0.4478 -0.2223] |
# |     10    | [ 0.6877  0.4478 -0.2223] | [-1  3 -1] | 0.8781 | [ 0.6755  0.4844 -0.2345] |
# |     11    | [ 0.6755  0.4844 -0.2345] | [-1  2  1] | 0.0588 | [ 0.5814  0.6726 -0.1404] |
# |     12    | [ 0.5814  0.6726 -0.1404] | [-1  3  2] | 1.1558 | [ 0.597   0.6259 -0.1715] |
# +-----------+---------------------------+------------+--------+---------------------------+