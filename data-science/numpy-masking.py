import numpy as np

# create array with 16 integers
b = np.arange(16)
b.shape = (4, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

# create mask with True
mask = np.ones(4, dtype=bool)       # [ True  True  True  True]

# get diagonal
b[mask, mask]                       # [ 0  5 10 15]

# create mask with both True and False
another_mask = np.array([[1, 0, 1, 1], [False, True, False, False], [0, 0, 1, 0], [0, 1, 1, 1]], dtype=bool)
# [[ True False  True  True]
#  [False  True False False]
#  [False False  True False]
#  [False  True  True  True]]

b[another_mask]                     # [ 0  2  3  5 10 13 14 15]

# create mask with conditional
conditional_mask = (b >= 9)
b[conditional_mask]                 # [ 9 10 11 12 13 14 15]

# get all values smaller than 9
b[b < 9]                            # [0 1 2 3 4 5 6 7 8]

# get all values smaller than 5 or larger than 10
b[(b < 5) | (b > 10)]               # [ 0  1  2  3  4 11 12 13 14 15]

# where
b[np.where(b > 10)]                 # [11 12 13 14 15]

# get all columns with a value less than 3
b[:, np.where(b < 3)[1]]
# [[ 0  1  2]
#  [ 4  5  6]
#  [ 8  9 10]
#  [12 13 14]]

'''
Michael Sjoeberg
2018-11-05
https://github.com/michaelsjoeberg/python-playground/blob/master/data-science/numpy-masking.py
'''