# Power digit sum
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
#
# https://projecteuler.net/problem=16

def pow_sum(n, p):
    return sum(list(map(int, list(str(n ** p)))))

assert pow_sum(2, 15) == 26

print(pow_sum(2, 1000))
# 1366