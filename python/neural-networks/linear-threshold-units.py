# https://en.wikipedia.org/wiki/Artificial_neuron
import numpy as np

# transfer function
# -----------------------------------------------------------
# heaviside step function (https://en.wikipedia.org/wiki/Heaviside_step_function)
def H(x, w, threshold=1):
    wx = np.dot(w, x)

    if (wx >= threshold):
        return 1
    # optional
    # elif (wx == threshold):
    #     return 0.5
    else:
        return 0

assert (H([0.1, -0.5, 0.4], [0.1, -0.5, 0.4], 0) == 1)
assert (H([0.1, 0.5, 0.4], [0.1, -0.5, 0.4], 0) == 0)
# optional
# assert (H([0, 0, 0], [0, 0, 0], 0) == 0.5)

# logical AND
threshold = 1.5

print(H([0, 0], [1, 1], threshold)) # 0
print(H([0, 1], [1, 1], threshold)) # 0
print(H([1, 0], [1, 1], threshold)) # 0
print(H([1, 1], [1, 1], threshold)) # 1

# logical NOT
threshold = -0.5

print(H([0], [-1], threshold)) # 1
print(H([1], [-1], threshold)) # 0

# logical OR
threshold = 0.5

print(H([0, 0], [1, 1], threshold)) # 0
print(H([0, 1], [1, 1], threshold)) # 1
print(H([1, 0], [1, 1], threshold)) # 1
print(H([1, 1], [1, 1], threshold)) # 1

# combination: (A AND NOT B) OR (A AND C) OR (NOT B AND C)
threshold = 1

print(H([0, 0, 0], [2, -2, 2], threshold)) # 0
print(H([1, 0, 0], [2, -2, 2], threshold)) # 1
print(H([0, 1, 0], [2, -2, 2], threshold)) # 0