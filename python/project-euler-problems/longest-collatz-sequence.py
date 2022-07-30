# Longest Collatz sequence
#
# The following iterative sequence is defined for the set of positive integers:
#
#   n -> n / 2 (n is even)
#   n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
#   13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
# that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# https://projecteuler.net/problem=14

def collatz(seq_lst, n):
    # append starting value
    seq_lst.append(int(n))
    while n > 1:
        # even
        if n % 2 == 0:
            n = n / 2
            seq_lst.append(int(n))
        # odd
        else:
            n = 3 * n + 1
            seq_lst.append(int(n))

    return seq_lst

assert collatz([], 13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

# solution (slow)

MAX_RANGE = 1000000

longest = (0, 0)

for n in range(MAX_RANGE):
    seq = collatz([], n)
    if len(seq) > longest[1]:
        longest = (n, len(seq))

print(longest[0])
# 837799