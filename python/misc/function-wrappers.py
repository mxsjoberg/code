"""
Function wrappers can be used to modify behavior of function
or method. The wraps decorator copies over the function name,
docstring, and arguments list to the wrapper function. This
is very useful for debugging and logging.
"""

from functools import wraps

def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"call to {func.__name__}, args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logging
def power(base, exp): return base ** exp

power(2, 3) # call to power, args: (2, 3), kwargs: {}
