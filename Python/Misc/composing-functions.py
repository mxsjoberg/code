# 2023-08

import functools
import operator

def compose(a, b): return lambda x: a(b(x))

def square(x): return x * x

def double(x): return x * 2

# double then square
op = compose(square, double)
print(op(5))
# 100

# passing operator as argument
numbers = [1, 2, 3, 4, 5]
print(functools.reduce(operator.add, numbers))
# 15