# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?
#
# https://projecteuler.net/problem=3

# test
number = 13195 
result = list()

factor = number - 1
while factor > 1:
    if number % factor == 0:
        # factor
        subfactor = factor - 1
        while subfactor > 1:
            if factor % subfactor == 0:
                break

            subfactor -= 1

        if subfactor == 1:
            result.append(factor)

    factor -= 1

assert(max(result) == 29)

# solution (too slow)
# number = 600851475143
# result = list()

# factor = number - 1
# while factor > 1:
#   if number % factor == 0:
#       # factor
#       subfactor = factor - 1
#       while subfactor > 1:
#           if factor % subfactor == 0:
#               break

#           subfactor -= 1

#       if subfactor == 1:
#           print(factor)
#           result.append(factor)

#   factor -= 1

# print(max(result))

# solution (faster)
import math

number = 600851475143
result = list()

while number % 2 == 0:
    result.append(2)
    number = number / 2

for i in range(3, int(math.sqrt(number)) + 1, 2):
    while number % i == 0:
        result.append(i)
        number = number / i

if number > 2:
    result.append(number)

print(max(result))
# 6857