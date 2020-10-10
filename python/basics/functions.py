def function(arg):
    '''docstring'''

    # do something

    return

# example
def power(base, x):
    '''multiply base with itself x times'''

    return base ** x

power(2, 3)                 # 8
power.__doc__               # multiply base with itself x times

# default arguments
def power(base, x = 3):
    return base ** x

power(2)                    # 8

# multiple return values
def power(base, x):
    result = base ** x

    return result, base

result, base = power(2, 3)      # (8, 2)

'''
Michael Sjoeberg
2018-11-05
https://github.com/michaelsjoeberg/python-playground/blob/master/basics/functions.py
'''