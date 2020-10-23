# 10001st prime
#
# By listing the first six prime numbers: 2, 3, 
# 5, 7, 11, and 13, we can see that the 6th prime 
# is 13.
#
# What is the 10001st prime number?
#
# https://projecteuler.net/problem=7

# import math
import numpy as np

# test (too slow)

# algorithm:
# π(n) = (sum from j=2 to n) [ ((j-1)! + 1)/j - [(j-1)!/j] ]
# nth prime = 1 + (sum from m=1 to j=2 ** n) [ [ n/(1 + π(m)) ]1/n ]
# [x] is floor function

# def pi(n):
#   pi_n = 0
#   for j in range(n + 1):
#       if j < 2:
#           pass
#       else:
#           pi_n += math.floor(((math.factorial(j - 1) + 1) // j) - math.floor(math.factorial(j - 1) // j))

#   return pi_n

# def n_prime(n):
#   n_prime = 0
#   for m in range(2 ** n + 1):
#       if m < 1:
#           pass
#       else:
#           n_prime += math.floor(math.floor(n // (1 + pi(m))) ** (1 / n))
#   n_prime += 1
#   return n_prime

# assert(n_prime(6) == 13)

# solution
MAX_SIZE = 1000000

# sieve of eratosthenes (genius)
def SOE(primelst):
    is_prime = np.ones(MAX_SIZE)
    
    prime = 2
    while (prime * prime) < MAX_SIZE:
        if is_prime[prime] == True:
            i = (prime * prime)
            while i < MAX_SIZE:
                is_prime[i] = 0
                i += prime
        prime += 1

    prime = 2
    while prime < MAX_SIZE:
        if is_prime[prime]:
            primelst.append(prime)

        prime += 1

    return primelst

result = SOE([])

n = 10001
print(result[n - 1])
# 104743