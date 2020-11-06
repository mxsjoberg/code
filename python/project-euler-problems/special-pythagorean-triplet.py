# Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three 
# natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2.
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet 
# for which a + b + c = 1000. Find the product 
# abc.
#
# https://projecteuler.net/problem=9

import numpy as np

# test
MAX_N = 500
def brute(MAX_N):
    '''it is not pretty, but it works'''
    for a in range(MAX_N):
        for b in range(MAX_N):
            for c in range(MAX_N):
                if (a < b and b < c) and (a ** 2 + b ** 2 == c ** 2) and (a + b + c == 1000):
                    return (a, b, c), a * b * c

    return 0

triplet, result = brute(MAX_N)

print(triplet)
# (200, 375, 425)
print(result)
# 31875000