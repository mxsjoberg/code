# 2023-08

"""
A partial function is a function with some arguments already
filled in. This is useful for creating new functions from
existing functions.
"""

from functools import partial

def power(base, exp): return base ** exp

# partial functions
square = partial(power, exp=2)
cube = partial(power, exp=3)

print(square(2))
# 4
print(cube(2))
# 8

# partial functions with map
numbers = [1, 2, 3, 4, 5]

print(list(map(square, numbers)))
# [1, 4, 9, 16, 25]
print(list(map(cube, numbers)))
# [1, 8, 27, 64, 125]
