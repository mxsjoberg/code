import numpy as np

## basics

a = [60, 28, 49, 81]
b = [55, 634, 704, 2020]

# create numpy array
A = np.array(a, dtype='i')
# print(A)
# [60 28 49 81]

AB = np.array([a, b])
# print(AB)
# [[  60   28   49   81]
#  [  55  634  704 2020]]

print(AB.ndim)
# 2
print(AB.shape)
# (2, 4)

arr_zero = np.zeros(4)
# print(arr_zero)
# [0. 0. 0. 0.]

arr_ones = np.ones((2, 3))
# print(arr_ones)
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]

arr_range = np.arange(0, 10)
# print(arr_range)
# [0 1 2 3 4 5 6 7 8 9]

arr_linspace = np.linspace(0, 1, 5)
# print(arr_linspace)
# [0.   0.25 0.5  0.75 1.  ]

arr_log = np.logspace(0, 1, 5)
# print(arr_log)
# [ 1.          1.77827941  3.16227766  5.62341325 10.        ]

# slicing
print(A[1:3])
# [28 49]
print(AB[0:2, 2:4])
# [[  49   81]
#  [ 704 2020]]

# reverse order
print(A[::-1])
# [81 49 28 60]

# operations
print(arr_range.mean())
# 4.5
print(arr_range.sum())
# 45
print(AB.min())
# 28
print(AB.max())
# 2020
print(np.sin(AB))
# [[-0.30481062  0.27090579 -0.95375265 -0.62988799]
#  [-0.99975517 -0.56605794  0.27947339  0.04406199]]
print(np.multiply(a, b))
# [  3300  17752  34496 163620]
print(np.sqrt(b))
# [ 7.41619849 25.17935662 26.53299832 44.94441011]

# min value in each column
print(np.minimum(a, b))
# [55 28 49 81]

# sum of axis (columns)
print(np.sum(AB, axis=1))
# [ 218 3413]

## indexing

# create array with 8 integers
A = 2 * np.arange(8)**2 + 1
# print(A)
# [ 1  3  9 19 33 51 73 99]

# create array with 16 integers
B = np.arange(16)
B.shape = (4, 4)
# print(B)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

print(A[[3, -1, 1]])
# [19 99  3]
print(B[:, [2, -1, 0]])
# [[ 2  3  0]
#  [ 6  7  4]
#  [10 11  8]
#  [14 15 12]]

# elements from A at indices given by fibonacci sequence
fibseq = np.array([0, 1, 1, 2, 3])
# print(A[fibseq])
# [ 1  3  3  9 19]

# diagonal
i = np.arange(4)
print(B[i, i])
# [ 0  5 10 15]

# diagonal of part
print(B[i[:3], i[:3] + 1])
# [ 1  6 11]

## masking

# create array with 16 integers
C = np.arange(16)
C.shape = (4, 4)
# print(C)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

# create mask with True
mask = np.ones(4, dtype=bool)
# print(mask)
# [ True  True  True  True]

# diagonal
print(C[mask, mask])
# [ 0  5 10 15]

# conditional mask
conditional = (C >= 9)
# print(C[conditional])
# [ 9 10 11 12 13 14 15]

# get all values smaller than 9
print(C[C < 9])
# [0 1 2 3 4 5 6 7 8]

# get all values smaller than 5 or larger than 10
print(C[(C < 5) | (C > 10)])
# [ 0  1  2  3  4 11 12 13 14 15]

# where
print(C[np.where(C > 10)])
# [11 12 13 14 15]

# get all columns with a value less than 3
print(C[:, np.where(C < 3)[1]])
# [[ 0  1  2]
#  [ 4  5  6]
#  [ 8  9 10]
#  [12 13 14]]

## operations

A = np.arange(6)
print(A)
# [0 1 2 3 4 5]
print(A + A)
# [ 0  2  4  6  8 10]
print(A - 1)
# [-1  0  1  2  3  4]
print(A * 6)
# [ 0  6 12 18 24 30]

# gradient
X = np.array([2, 4, 5])
Y = np.array([6, 2, 8])
print(np.gradient(X))
# [ 2.   1.5  1. ] 		=> (4 - 2) / 1, (5 - 2) / 2, (5 - 4)/ 1
print(np.gradient(Y))
# [-4.  1.  6.] 		=> (2 - 6) / 1, (8 - 6) / 2, (8 - 2)/ 1

# numerical derivative
print(np.gradient(Y) / np.gradient(X))
# [-2.          0.66666667  6.        ]

B = np.arange(4)
B.shape = (2, 2)
# print(B)
# [[0 1]
#  [2 3]]

v = np.array([[2],[4]])
# print(v)
# [[2]
#  [4]]

# scalar (multiplication)
print(B * v)
# [[ 0  2]
#  [ 8 12]]

# dot product
print(np.dot(B, v))
# [[ 4]
#  [16]]

# operations on higher dimensions
M = np.arange(12)
M.shape = (4, 3)
# print(M)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

v = np.array([16, 17, 18])

print(M + v)
# [[16 18 20]
#  [19 21 23]
#  [22 24 26]
#  [25 27 29]]
