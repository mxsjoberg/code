# https://en.wikipedia.org/wiki/Artificial_neuron
import numpy as np
# https://pypi.org/project/tabulate/
from tabulate import tabulate

# https://en.wikipedia.org/wiki/Heaviside_step_function
def H(x, w, threshold=1):
    wx = np.dot(w, x)
    if (wx >= threshold):
        return 1
    else:
        return 0

assert (H([0.1, -0.5, 0.4], [0.1, -0.5, 0.4], 0) == 1)
assert (H([0.1, 0.5, 0.4], [0.1, -0.5, 0.4], 0) == 0)

table = []

# logical AND
threshold = 1.5
table.append(['AND', [0, 0], [1, 1], threshold, H([0, 0], [1, 1], threshold)])
table.append(['AND', [0, 1], [1, 1], threshold, H([0, 1], [1, 1], threshold)])
table.append(['AND', [1, 0], [1, 1], threshold, H([1, 0], [1, 1], threshold)])
table.append(['AND', [1, 1], [1, 1], threshold, H([1, 1], [1, 1], threshold)])

# logical NOT
threshold = -0.5
table.append(['NOT', [0], [-1], threshold, H([0], [-1], threshold)])
table.append(['NOT', [1], [-1], threshold, H([1], [-1], threshold)])

# logical OR
threshold = 0.5
table.append(['OR', [0, 0], [1, 1], threshold, H([0, 0], [1, 1], threshold)])
table.append(['OR', [0, 1], [1, 1], threshold, H([0, 1], [1, 1], threshold)])
table.append(['OR', [1, 0], [1, 1], threshold, H([1, 0], [1, 1], threshold)])
table.append(['OR', [1, 1], [1, 1], threshold, H([1, 1], [1, 1], threshold)])

# combination: (A AND NOT B) OR (A AND C) OR (NOT B AND C)
threshold = 1
table.append(['COMBINATION', [0, 0, 0], [2, -2, 2], threshold, H([0, 0, 0], [2, -2, 2], threshold)])
table.append(['COMBINATION', [1, 0, 0], [2, -2, 2], threshold, H([1, 0, 0], [2, -2, 2], threshold)])
table.append(['COMBINATION', [0, 1, 0], [2, -2, 2], threshold, H([0, 1, 0], [2, -2, 2], threshold)])

print(tabulate(table, headers=['unit', 'x', 'w', 'threshold', 'output'], tablefmt="simple"))
# unit         x          w             threshold    output
# -----------  ---------  ----------  -----------  --------
# AND          [0, 0]     [1, 1]              1.5         0
# AND          [0, 1]     [1, 1]              1.5         0
# AND          [1, 0]     [1, 1]              1.5         0
# AND          [1, 1]     [1, 1]              1.5         1
# NOT          [0]        [-1]               -0.5         1
# NOT          [1]        [-1]               -0.5         0
# OR           [0, 0]     [1, 1]              0.5         0
# OR           [0, 1]     [1, 1]              0.5         1
# OR           [1, 0]     [1, 1]              0.5         1
# OR           [1, 1]     [1, 1]              0.5         1
# COMBINATION  [0, 0, 0]  [2, -2, 2]          1           0
# COMBINATION  [1, 0, 0]  [2, -2, 2]          1           1
# COMBINATION  [0, 1, 0]  [2, -2, 2]          1           0