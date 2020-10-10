import numpy as np

# create array with 8 integers
a = 2 * np.arange(8)**2 + 1         # [ 1  3  9 19 33 51 73 99]

# create array with 16 integers
b = np.arange(16)
b.shape = (4, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

# fancy indexing
a[[3, -1, 1]]                       # [19 99  3]
b[:, [2, -1, 0]]
# [[ 2  3  0]
#  [ 6  7  4]
#  [10 11  8]
#  [14 15 12]]

# get fibonacci sequence
fib = np.array([0, 1, 1, 2, 3])
a[fib]                              # [ 1  3  3  9 19]
b[fib]
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]


# get diagonal
i = np.arange(4)
b[i, i]                             # [ 0  5 10 15]

# get diagonal of upper part
b[i[:3], i[:3] + 1]                 # [ 1  6 11]

# get diagonal of lower part
b[i[1:], i[1:] - 1]                 # [ 4  9 14]

'''
Michael Sjoeberg
2018-11-05
https://github.com/michaelsjoeberg/python-playground/blob/master/data-science/numpy-indexing.py
'''