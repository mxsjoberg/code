# Smallest multiple
#
# 2520 is the smallest number that can be divided by 
# each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?
#
# https://projecteuler.net/problem=5

# test
MAX_ITER = 10000

number = 1
nlst = list(range(1, 11))
result = -1
while number < MAX_ITER:
    divisible = True

    for n in nlst:
        if number % n != 0:
            divisible = False
            break

    if divisible:
        result = number
        break

    number += 1

assert(result == 2520)

# solution
MAX_ITER = 1000000000

number = 1
nlst = list(range(11, 21))
result = -1
while number < MAX_ITER:
    divisible = True

    for n in nlst:
        if number % n != 0:
            divisible = False
            break

    if divisible:
        result = number
        break

    number += 1

print(result)
# 232792560