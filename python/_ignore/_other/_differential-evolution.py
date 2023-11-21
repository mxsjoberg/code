# https://en.wikipedia.org/wiki/Differential_evolution

# https://en.wikipedia.org/wiki/Rosenbrock_function
from scipy.optimize import rosen, differential_evolution

bounds = [(0, 2), (0, 2), (0, 2), (0, 2), (0, 2)]
result = differential_evolution(rosen, bounds)

print(result.x)
print(result.fun)