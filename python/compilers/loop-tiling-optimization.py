import random
import timeit

# timeit.template = """
# def inner(_it, _timer{init}):
#     from tqdm import tqdm
#     {setup}
#     _t0 = _timer()
#     for _i in tqdm(_it, total=_it.__length_hint__()):
#         {stmt}
#     _t1 = _timer()
#     return _t1 - _t0
# """

# matrix multiplication
def matmul(A, B):
    m, n, p = len(A), len(A[0]), len(B[0])
    result = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]

assert matmul(A, B) == [[30, 24, 18], [84, 69, 54], [138, 114, 90]]

# tiling
TILE_SIZE = 100
def matmul_tiled(A, B):
    m, n, p = len(A), len(A[0]), len(B[0])
    result = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(0, m, TILE_SIZE):
        for j in range(0, p, TILE_SIZE):
            for k in range(0, n, TILE_SIZE):
                for ii in range(i, min(i + TILE_SIZE, m)):
                    for jj in range(j, min(j + TILE_SIZE, p)):
                        for kk in range(k, min(k + TILE_SIZE, n)):
                            result[ii][jj] += A[ii][kk] * B[kk][jj]

    return result

assert matmul_tiled(A, B) == [[30, 24, 18], [84, 69, 54], [138, 114, 90]]

A = [[random.random() for _ in range(200)] for _ in range(200)]
B = [[random.random() for _ in range(200)] for _ in range(200)]

print(timeit.timeit(lambda: matmul(A, B), number=10))
# 6.854414212051779
print(timeit.timeit(lambda: matmul_tiled(A, B), number=10))
# 6.588905839016661
