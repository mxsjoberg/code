# Lattice paths
#
# Starting in the top left corner of a 2×2 grid, and only being able to 
# move to the right and down, there are exactly 6 routes to the bottom 
# right corner.
#
# How many such routes are there through a 20×20 grid?
#
# https://projecteuler.net/problem=15

# test

# pascal triangle (2x2 -> 3x3 grid line): 6 paths
# 1 1 1
# 1 2 3
# 1 3 6

# pascal triangle (3x3 -> 4x4 grid line) : 20 paths
# 1 1  1  1
# 1 2  3  4
# 1 3  6 10
# 1 4 10 20

import numpy as np

# https://en.wikipedia.org/wiki/Pascal%27s_triangle
def pascal_triangle(size):
    grid = np.ones((size, size))
    for i in range(size):
        if i > 0:
            for j in range(size):
                if j > 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid

assert int(pascal_triangle(3)[2][2]) == 6
assert int(pascal_triangle(4)[3][3]) == 20

print(int(pascal_triangle(21)[20][20]))
# 137846528820