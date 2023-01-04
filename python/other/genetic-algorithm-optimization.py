# https://en.wikipedia.org/wiki/Genetic_algorithm
import random
import math
# https://pypi.org/project/tabulate/
from tabulate import tabulate

# configuration variables
# ---------------------------------------------
M_BITS = 4
N_POP = 4
N_KEEP = 2
MUTATE_RATE = 0.1

#random.seed(1234)

# generations
MAX_GEN = 10000

# cost function
# def f(x, y):
#     return x * y

def f(x, y):
    return -x * (y / 2 - 10)

# range
x_range = [10, 20]
y_range = [-5, 7]

# crossover
crossover = [3, 6]

# genetic algorithm functions
# ---------------------------------------------
# encoding equation: B = (x - x_low) / [(x_high - x_low) / (2 ** m - 1)]
def encode(x, x_low, x_high, m):
    decimal = round((x - x_low) / ((x_high - x_low) / (2 ** m - 1)))
    binary = []
    while decimal >= 1:
        if decimal % 2 == 1:
            binary.append(1)
        else:
            binary.append(0)
        decimal = math.floor(decimal / 2)
    while len(binary) < 4:
        binary.append(0)

    return list(reversed(binary))

assert encode(9, -10, 14, 5) == [1, 1, 0, 0, 1]

# decoding equation: x = x_low + B * ( (x_high - x_low) / ((2 ** m) - 1) )
def decode(B, x_low, x_high, m):
    decoded = x_low + int((''.join(map(str, B))), 2) * ((x_high - x_low) / ((2 ** m) - 1))
    
    return decoded

assert round(decode([1, 0, 0, 0], 10, 20, 4), 2) == 15.33
assert int(decode([1, 1, 0, 0, 1], -10, 14, 5)) == 9

# generate initial population
def generate_population(n_pop, x_range, y_range, m_bits, debug=False):
    if debug: random.seed(10)
    pop_lst = []
    for i in range(n_pop):
        x = random.randint(x_range[0], x_range[1])
        y = random.randint(y_range[0], y_range[1])
        # encoded values
        x_encoded = encode(x, x_range[0], x_range[1], m_bits)
        y_encoded = encode(y, y_range[0], y_range[1], m_bits)
        # decoded values
        x_decoded = round(decode(x_encoded, x_range[0], x_range[1], m_bits), 2)
        y_decoded = round(decode(y_encoded, y_range[0], y_range[1], m_bits), 2)
        # determine initial cost
        cost = round(f(x_decoded, y_decoded), 2)
        # append to list
        pop_lst.append([i, x_encoded + y_encoded, [x_decoded, y_decoded], cost])
    # sort on cost
    pop_lst.sort(key = lambda x: x[3])
    # update index
    for i in range(len(pop_lst)):
        pop_lst[i][0] = i

    return pop_lst

# test
example_population = generate_population(6, [5, 20], [-5, 15], 4, True)
print(tabulate(example_population, headers=['n', 'encoding', 'decoded x, y', 'cost'], floatfmt=".3f", tablefmt="simple"), end="\n\n")
#   n  encoding                  decoded x, y       cost
# ---  ------------------------  --------------  -------
#   0  [1, 0, 0, 0, 1, 1, 1, 1]  [13.0, 15.0]     32.500
#   1  [0, 0, 0, 1, 1, 0, 1, 0]  [6.0, 8.33]      35.010
#   2  [0, 0, 0, 0, 0, 1, 0, 0]  [5.0, 0.33]      49.180
#   3  [1, 1, 1, 1, 1, 1, 1, 0]  [20.0, 13.67]    63.300
#   4  [1, 1, 1, 0, 1, 0, 1, 1]  [19.0, 9.67]     98.140
#   5  [0, 1, 0, 1, 0, 0, 0, 1]  [10.0, -3.67]   118.350

# generate offsprings
def generate_offsprings(population, crossover):
    n = 0
    offsprings_lst = []
    while n < len(population):
        offsprings_lst.append(population[n][1][0:crossover[0]] + population[n + 1][1][crossover[0]:crossover[1]] + population[n][1][crossover[1]:])
        offsprings_lst.append(population[n + 1][1][0:crossover[0]] + population[n][1][crossover[0]:crossover[1]] + population[n + 1][1][crossover[1]:])
        # pair-wise
        n += 2

    return offsprings_lst

# mutate
def mutate(offsprings, mu, m_bits):
    nbits = round(mu * (len(offsprings) * m_bits * 2))
    for i in range(nbits):
        offspring = random.randint(0, len(offsprings) - 1)
        bit = random.randint(0, m_bits * 2 - 1)
        # swap bits
        if offsprings[offspring][bit] == 1:
            offsprings[offspring][bit] = 0
        else:
            offsprings[offspring][bit] = 1

    return offsprings

# update population
def update_population(current_population, offsprings, keep, x_range, y_range, m_bits):
    offsprings_lst = []
    for i in range(len(offsprings)):
        # decoded values
        x_decoded = round(decode(offsprings[i][:4], x_range[0], x_range[1], m_bits), 2)
        y_decoded = round(decode(offsprings[i][4:], y_range[0], y_range[1], m_bits), 2)
        # determine initial cost
        cost = round(f(x_decoded, y_decoded), 2)
        # append to list
        offsprings_lst.append([i, offsprings[i], [x_decoded, y_decoded], cost])
    # sort on cost
    offsprings_lst.sort(key = lambda x: x[3])
    # update index
    for i in range(len(offsprings_lst)):
        offsprings_lst[i][0] = i
    # discard current population
    current_population[keep:] = offsprings_lst[:keep]
    # sort on cost
    current_population.sort(key = lambda x: x[3])
    # update index
    for i in range(len(current_population)):
        current_population[i][0] = i

    return current_population

# generate population
# ---------------------------------------------
current_population = generate_population(N_POP, x_range, y_range, M_BITS)
print(tabulate(current_population, headers=['n', 'encoding', 'decoded x, y', 'cost'], floatfmt=".3f", tablefmt="github"), end="\n\n")
# |   n | encoding                 | decoded x, y   |    cost |
# |-----|--------------------------|----------------|---------|
# |   0 | [0, 0, 1, 1, 0, 0, 0, 0] | [12.0, -5.0]   | -60.000 |
# |   1 | [0, 1, 0, 0, 0, 1, 0, 0] | [12.67, -1.8]  | -22.810 |
# |   2 | [0, 0, 1, 0, 0, 1, 0, 0] | [11.33, -1.8]  | -20.390 |
# |   3 | [1, 0, 1, 0, 1, 1, 1, 0] | [16.67, 6.2]   | 103.350 |

for i in range(MAX_GEN):
    # generate offsprings
    offsprings = generate_offsprings(current_population, crossover)
    # mutate
    offsprings = mutate(offsprings, MUTATE_RATE, M_BITS)
    # update population
    current_population = update_population(current_population, offsprings, N_KEEP, x_range, y_range, M_BITS)

print(tabulate(current_population, headers=['n', 'encoding', 'decoded x, y', 'cost'], floatfmt=".3f", tablefmt="github"), end="\n\n")
# |   n | encoding                 | decoded x, y   |     cost |
# |-----|--------------------------|----------------|----------|
# |   0 | [1, 1, 1, 1, 0, 0, 0, 0] | [20.0, -5.0]   | -100.000 |
# |   1 | [1, 1, 1, 1, 0, 0, 0, 0] | [20.0, -5.0]   | -100.000 |
# |   2 | [1, 1, 1, 1, 0, 0, 0, 0] | [20.0, -5.0]   | -100.000 |
# |   3 | [1, 1, 1, 1, 0, 0, 0, 0] | [20.0, -5.0]   | -100.000 |
