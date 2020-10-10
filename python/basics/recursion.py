
# EXAMPLE: Countdown

def countdown(n):
    if n <= 0:
        print("Done.")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
# 5
# 4
# 3
# 2
# 1
# Done.

'''
Michael Sjoeberg
2019-09-12
https://github.com/michaelsjoeberg/python-playground/blob/master/basics/recursion.py
'''