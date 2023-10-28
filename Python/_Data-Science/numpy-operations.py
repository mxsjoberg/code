import numpy as np

a = np.arange(6)                    # [0 1 2 3 4 5]
a + a                               # [ 0  2  4  6  8 10]
a - 1                               # [-1  0  1  2  3  4]
a * 6                               # [ 0  6 12 18 24 30]

# gradient
x = np.array([2, 4, 5])             # [2 4 5]
y = np.array([6, 2, 8])             # [6, 2, 8]
np.gradient(x)                      # [ 2.   1.5  1. ]      -> (4 - 2) / 1, (5 - 2) / 2, (5 - 4)/ 1
np.gradient(y)                      # [-4.  1.  6.]         -> (2 - 6) / 1, (8 - 6) / 2, (8 - 2)/ 1

# numerical derivative
np.gradient(y) / np.gradient(x)
# [-2.          0.66666667  6.        ]

# broadcasting
b = np.arange(4)
b.shape = (2, 2)
# [[0 1]
#  [2 3]]

v = np.array([[2],[4]])
# [[2]
#  [4]]

# scalar (multiplication)
b * v
# [[ 0  2]
#  [ 8 12]]

# dot product
np.dot(b, v)
# [[ 4]
#  [16]]

# operations on higher dimensions
matrix = np.arange(12)
matrix.shape = (4, 3)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

row = np.array([16, 17, 18])
# [16 17 18]

matrix + row
# [[16 18 20]
#  [19 21 23]
#  [22 24 26]
#  [25 27 29]]