# 2023-08

"""
A simple implementation of linear layer followed by a
ReLU activation function.
"""

import numpy as np

dtype = "float32"

# numpy
a_np = np.random.rand(128, 128).astype(dtype)
b_np = np.random.rand(128, 128).astype(dtype)
# matmul -> relu
c_mm_relu = np.maximum(a_np @ b_np, 0)

# implementation
def mm_relu(A: np.ndarray, B: np.ndarray, C: np.ndarray):
    # A, B, C: 128x128
    Y = np.empty((128, 128), dtype=dtype)
    # matmul
    for i in range(128):
        for j in range(128):
            for k in range(128):
                if k == 0: Y[i, j] = 0
                Y[i, j] += A[i, k] * B[k, j]
    # relu
    for i in range(128):
        for j in range(128):
            C[i, j] = max(Y[i, j], 0)

# test
c_np = np.empty((128, 128), dtype=dtype)
mm_relu(a_np, b_np, c_np)
# check within tolerance
np.testing.assert_allclose(c_mm_relu, c_np, rtol=1e-5)
