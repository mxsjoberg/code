# 2018-06

def power(base, x = 1):
    """base to the x-th power"""

    i = 0
    while i < x - 1:
        base += base
        i += 1

    return base

print(power(2, 8))
# 256
print(power.__doc__)
# base to the x-th power

print(power(2))
# 2