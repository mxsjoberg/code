import numpy as np

a = [60, 28, 49, 81]
b = [55, 634, 704, 2020]

# create numpy array with list, specifying type as integer
array_single = np.array(a, dtype='i')
array_single                    # [60 28 49 81]

# create numpy array with many lists
array_many = np.array([a, b])
array_many
# [[  60   28   49   81]
#  [  55  634  704 2020]]

# dimension and shape
array_many.ndim                 # 2
array_many.shape                # (2, 4)

# create numpy array with zeros
array_zeros = np.zeros(4)
array_zeros                     # [ 0.  0.  0.  0.]

# create 2x3 numpy array with ones
array_ones = np.ones((2, 3))
array_ones
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]

# create numpy array with range from 0 to 50
array_range = np.arange(0, 50)
array_range
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
#  25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]

# create numpy array with ten numbers spaced between 0 and 10 (linear)
array_linear = np.linspace(0, 1, 10)
array_linear
# [ 0.          0.11111111  0.22222222  0.33333333  0.44444444  0.55555556
#   0.66666667  0.77777778  0.88888889  1.        ]

# create numpy array with ten numbers spaced between 1 and 10 (logarithmic)
array_log = np.logspace(0, 1, 10)
array_log
# [  1.           1.29154967   1.66810054   2.15443469   2.7825594
#    3.59381366   4.64158883   5.9948425    7.74263683  10.        ]

# get second to third value
array_single[1:3]               # [28 49]

# reverse order
array_single[::-1]              # [81 49 28 60]

# multidimensional slicing (3rd and 4th column, both rows)
array_many[0:2, 2:4]
# [[  49   81]
#  [ 704 2020]]

# array operations
array_range.mean()              # 24.5
array_range.sum()               # 1225
array_many.min()                # 28
array_many.max()                # 2020

np.sin(array_many)
# [[-0.30481062  0.27090579 -0.95375265 -0.62988799]
#  [-0.99975517 -0.56605794  0.27947339  0.04406199]]

np.multiply(a, b)               # [3300  17752  34496 163620]
np.sqrt(b)                      # [7.41619849  25.17935662  26.53299832  44.94441011]

# minimum value in each column
np.minimum(a, b)                # [55 28 49 81]

# sum of axis (columns)
np.sum(array_many, axis=1)      # [218 3413]

'''
Michael Sjoeberg
2018-11-05
https://github.com/michaelsjoeberg/python-playground/blob/master/data-science/numpy-arrays.py
'''