# Largest palindrome product
#
# A palindromic number reads the same both ways. The 
# largest palindrome made from the product of two 2-digit 
# numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# https://projecteuler.net/problem=4

# test
MAX_2 = 100

nlst = list(range(MAX_2))[80:]
result = list()
for i in nlst:
    for j in nlst:
        product = i * j
        if list(str(product)) == list(str(product))[::-1]:
            result.append(product)

assert(max(result) == 9009)

# solution
MAX_2 = 1000

nlst = list(range(MAX_2))[800:]
result = list()
for i in nlst:
    for j in nlst:
        product = i * j
        if list(str(product)) == list(str(product))[::-1]:
            result.append(product)

print(max(result))
# 906609