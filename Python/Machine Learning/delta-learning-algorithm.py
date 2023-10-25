# https://en.wikipedia.org/wiki/Delta_rule
import numpy as np
# https://pypi.org/project/tabulate/
from tabulate import tabulate

# initial weights
w = [1, 0, 0]
# learning rate
n = 1
# iterations
iterations = 12

# dataset
X = [[1, 0, 2],
     [1, 1, 2],
     [1, 2, 1],
     [1, -3, 1],
     [1, -2, -1],
     [1, -3, -2]]
# classes
t = [1, 1, 1, 0, 0, 0]

# https://en.wikipedia.org/wiki/Heaviside_step_function
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
result = []
for o in range(int(iterations / len(X))):
    for i in range(len(X)):
        if ((i + 1 + (len(X) * o)) > iterations):
            break
        w_prev = w
        x = X[i]
        y = transfer_function(w, x)
        # calculate update part
        update = np.zeros(len(x))
        for j in range(len(x)):
            update[j] = n * (t[i] - y) * x[j]
        # add update part to w
        w = np.add(w, update)
        # append to result
        result.append([
            # iteration
            i + 1 + (len(X) * o),
            # w
            list(w_prev),
            # x
            x,
            # y = H(wx)
            y,
            # t
            t[i],
            # w_new
            list(w)]
        )

print(tabulate(result, headers=['i', 'w', 'x', 'y = H(wx)', 't', 'w_new'], tablefmt="simple"))
#   i  w                 x              y = H(wx)    t  w_new
# ---  ----------------  -----------  -----------  ---  ----------------
#   1  [1, 0, 0]         [1, 0, 2]              1    1  [1.0, 0.0, 0.0]
#   2  [1.0, 0.0, 0.0]   [1, 1, 2]              1    1  [1.0, 0.0, 0.0]
#   3  [1.0, 0.0, 0.0]   [1, 2, 1]              1    1  [1.0, 0.0, 0.0]
#   4  [1.0, 0.0, 0.0]   [1, -3, 1]             1    0  [0.0, 3.0, -1.0]
#   5  [0.0, 3.0, -1.0]  [1, -2, -1]            0    0  [0.0, 3.0, -1.0]
#   6  [0.0, 3.0, -1.0]  [1, -3, -2]            0    0  [0.0, 3.0, -1.0]
#   7  [0.0, 3.0, -1.0]  [1, 0, 2]              0    1  [1.0, 3.0, 1.0]
#   8  [1.0, 3.0, 1.0]   [1, 1, 2]              1    1  [1.0, 3.0, 1.0]
#   9  [1.0, 3.0, 1.0]   [1, 2, 1]              1    1  [1.0, 3.0, 1.0]
#  10  [1.0, 3.0, 1.0]   [1, -3, 1]             0    0  [1.0, 3.0, 1.0]
#  11  [1.0, 3.0, 1.0]   [1, -2, -1]            0    0  [1.0, 3.0, 1.0]
#  12  [1.0, 3.0, 1.0]   [1, -3, -2]            0    0  [1.0, 3.0, 1.0]
