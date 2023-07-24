# https://www.cs.princeton.edu/courses/archive/spring13/cos511/scribe_notes/0411.pdf
import numpy as np
# https://pypi.org/project/tabulate/
from tabulate import tabulate

# initial values
w = [1, 0, 0]
# margin vector
v = [1, 1, 1, 1, 1, 1]
# learning rate
n = 0.1
# iterations
iterations = 12

# dataset
X = [[0, 2], [1, 2], [2, 1], [-3, 1], [-2, 1], [-3, 2]]
Y = [[1, 0, 2], [1, 1, 2], [1, 2, 1], [-1, 3, -1], [-1, 2, 1], [-1, 3, 2]]

# sequential widrow-hoff learning algorithm
result = []
for o in range(int(iterations / len(Y))):
    for i in range(len(Y)):
        w_prev = w
        y = Y[i]
        # calculate wy
        wy = np.dot(w, y)
        # calculate update part
        update = np.zeros(len(y))
        for j in range(len(y)):
            update[j] = n * (v[i] - wy) * y[j]
        # add update part to a
        w = np.add(w, update)
        # append result
        result.append([
            # i
            i + 1 + (len(Y) * o),
            # w
            [round(x, 3) for x in w_prev],
            # y
            list(y),
            # wy
            round(wy, 3),
            # w_new
            [round(x, 3) for x in w]
        ])

print(tabulate(result, headers=['i', 'w', 'y', 'wy', 'w_new'], tablefmt="simple"))
#   i  w                       y                wy  w_new
# ---  ----------------------  -----------  ------  ----------------------
#   1  [1, 0, 0]               [1, 0, 2]     1      [1.0, 0.0, 0.0]
#   2  [1.0, 0.0, 0.0]         [1, 1, 2]     1      [1.0, 0.0, 0.0]
#   3  [1.0, 0.0, 0.0]         [1, 2, 1]     1      [1.0, 0.0, 0.0]
#   4  [1.0, 0.0, 0.0]         [-1, 3, -1]  -1      [0.8, 0.6, -0.2]
#   5  [0.8, 0.6, -0.2]        [-1, 2, 1]    0.2    [0.72, 0.76, -0.12]
#   6  [0.72, 0.76, -0.12]     [-1, 3, 2]    1.32   [0.752, 0.664, -0.184]
#   7  [0.752, 0.664, -0.184]  [1, 0, 2]     0.384  [0.814, 0.664, -0.061]
#   8  [0.814, 0.664, -0.061]  [1, 1, 2]     1.356  [0.778, 0.628, -0.132]
#   9  [0.778, 0.628, -0.132]  [1, 2, 1]     1.903  [0.688, 0.448, -0.222]
#  10  [0.688, 0.448, -0.222]  [-1, 3, -1]   0.878  [0.676, 0.484, -0.234]
#  11  [0.676, 0.484, -0.234]  [-1, 2, 1]    0.059  [0.581, 0.673, -0.14]
#  12  [0.581, 0.673, -0.14]   [-1, 3, 2]    1.156  [0.597, 0.626, -0.172]
