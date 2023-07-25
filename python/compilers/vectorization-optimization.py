import numpy as np
import timeit
from dis import dis

def add_arrays(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

# vectorized
def add_arrays_vectorized(a, b):
    return np.array(a) + np.array(b)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [9, 8, 7, 6, 5, 4, 3, 2, 1]

assert np.array(add_arrays(a, b)).all() == add_arrays_vectorized(a, b).all()

# test data
a = np.random.randint(0, 10, size=1000000)
b = np.random.randint(0, 10, size=1000000)

print(timeit.timeit(lambda: add_arrays(a, b), number=10))
# 2.4067575628869236
print(timeit.timeit(lambda: add_arrays_vectorized(a, b), number=10))
# 0.07865401287563145

dis(add_arrays)
# 4           0 RESUME                   0

# 5           2 BUILD_LIST               0
#             4 STORE_FAST               2 (result)

# 6           6 LOAD_GLOBAL              1 (NULL + range)
#            18 LOAD_GLOBAL              3 (NULL + len)
#            30 LOAD_FAST                0 (a)
#            32 PRECALL                  1
#            36 CALL                     1
#            46 PRECALL                  1
#            50 CALL                     1
#            60 GET_ITER
#       >>   62 FOR_ITER                38 (to 140)
#            64 STORE_FAST               3 (i)

# 7          66 LOAD_FAST                2 (result)
#            68 LOAD_METHOD              2 (append)
#            90 LOAD_FAST                0 (a)
#            92 LOAD_FAST                3 (i)
#            94 BINARY_SUBSCR
#           104 LOAD_FAST                1 (b)
#           106 LOAD_FAST                3 (i)
#           108 BINARY_SUBSCR
#           118 BINARY_OP                0 (+)
#           122 PRECALL                  1
#           126 CALL                     1
#           136 POP_TOP
#           138 JUMP_BACKWARD           39 (to 62)

# 8     >>  140 LOAD_FAST                2 (result)
#           142 RETURN_VALUE

dis(add_arrays_vectorized)
# 11           0 RESUME                   0

# 12           2 LOAD_GLOBAL              1 (NULL + np)
#             14 LOAD_ATTR                1 (array)
#             24 LOAD_FAST                0 (a)
#             26 PRECALL                  1
#             30 CALL                     1
#             40 LOAD_GLOBAL              1 (NULL + np)
#             52 LOAD_ATTR                1 (array)
#             62 LOAD_FAST                1 (b)
#             64 PRECALL                  1
#             68 CALL                     1
#             78 BINARY_OP                0 (+)
#             82 RETURN_VALUE