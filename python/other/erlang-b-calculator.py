# https://en.wikipedia.org/wiki/Erlang_(unit)#Erlang_B_formula
from math import factorial

def erlang(A, m):
    L = (A ** m) / factorial(m)
    sum_ = 0
    for n in range(m + 1): sum_ += (A ** n) / factorial(n)

    return (L / sum_)

print(erlang(90, 107))
# 0.008799105244742682