# Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are multiples 
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 
# 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# https://projecteuler.net/problem=1

# test
result = list()
for n in list(range(10))[1:]:
    if n % 3 == 0 or n % 5 == 0:
        result.append(n)

assert(sum(result) == 23)

# solution
result = list()
for n in list(range(1000))[1:]:
    if n % 3 == 0 or n % 5 == 0:
        result.append(n)

print(sum(result))
# 233168