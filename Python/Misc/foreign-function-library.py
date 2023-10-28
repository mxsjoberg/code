# 2023-08

"""
A foreign function library is a library written in
languages other than the language it is being called
from. E.g., a Python program calling function from C
library.
"""

"""
// _square.c
#include <stdio.h>

int square(int num) {
    return num * num;
}
// compile into shared library:
// $ gcc -shared -o _square.so -fPIC _square.c
"""

import ctypes

# load the shared library
square_lib = ctypes.CDLL('./_square.so')

# specify function return and argument types
square_lib.square.restype = ctypes.c_int
square_lib.square.argtypes = [ctypes.c_int]

# call the foreign function
num = 5
result = square_lib.square(num)

print(f"the square of {num} is {result}")
# the square of 5 is 25

# using C standard library functions
# https://gist.github.com/PewZ/8b473c2a6888c5c528635550d07c6186

libc = ctypes.CDLL('libc.dylib')
libc.printf(b"hello world\n")
# hello world
