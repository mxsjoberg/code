# BGA is a metaheuristic optimization algorithm inspired
# by the process of natural selection. It is a
# population-based algorithm that uses a genetic
# representation of the decision variables to search for
# the optimal solution.

import random
import math
# https://pypi.org/project/tabulate/
from tabulate import tabulate

random.seed(42)

# helper function to print as table
def print_as_table(population):
    table = tabulate(
        population,
        headers=['n', 'encoding', 'decoded x, y', 'cost'],
        floatfmt=".3f",
        tablefmt="simple"
    )
    print(table, end="\n\n")

def encode(x, x_low, x_high, m):
    """Encode decimal number into binary

    x (int)                 : decimal number
    x_low (int)             : lower bound of x
    x_high (int)            : upper bound of x
    m (int)                 : number of bits
    """
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

def decode(B, x_low, x_high, m):
    """Decode binary into decimal number

    B (list)                : binary number
    x_low (int)             : lower bound of x
    x_high (int)            : upper bound of x
    m (int)                 : number of bits
    """

    return x_low + int((''.join(map(str, B))), 2) * ((x_high - x_low) / ((2 ** m) - 1))

assert int(decode([1, 1, 0, 0, 1], -10, 14, 5)) == 9

def generate_population(f, n_pop, x_range, y_range, m_bits):
    """Generate initial population

    f (function)            : cost function
    n_pop (int)             : number of population
    x_range (list)          : range of x
    y_range (list)          : range of y
    m_bits (int)            : number of bits
    """
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

# example_population = generate_population(
#     f,
#     n_pop=6,
#     x_range=[5, 20],
#     y_range=[-5, 15],
#     m_bits=4
# )
# print_as_table(example_population)
#   n  encoding                  decoded x, y       cost
# ---  ------------------------  --------------  -------
#   0  [0, 0, 1, 0, 1, 1, 1, 0]  [7.0, 13.67]     22.160
#   1  [0, 0, 1, 1, 1, 1, 0, 1]  [8.0, 12.33]     30.680
#   2  [0, 0, 1, 1, 0, 0, 0, 0]  [8.0, -5.0]     100.000
#   3  [1, 0, 0, 0, 0, 1, 0, 1]  [13.0, 1.67]    119.140
#   4  [0, 1, 1, 1, 0, 0, 1, 1]  [12.0, -1.0]    126.000
#   5  [1, 1, 0, 1, 0, 0, 0, 1]  [18.0, -3.67]   213.030

def generate_offsprings(population, crossover):
    """Generate offsprings

    population (list)       : population
    crossover (list)        : crossover points
    """
    n = 0
    offsprings_lst = []
    while n < len(population):
        offsprings_lst.append(
            population[n][1][0:crossover[0]] +
            population[n + 1][1][crossover[0]:crossover[1]] +
            population[n][1][crossover[1]:]
        )
        offsprings_lst.append(
            population[n + 1][1][0:crossover[0]] +
            population[n][1][crossover[0]:crossover[1]] +
            population[n + 1][1][crossover[1]:]
        )
        # pair-wise
        n += 2

    return offsprings_lst

def mutate(offsprings, mu, m_bits):
    """Mutate offsprings

    offsprings (list)       : offsprings
    mu (float)              : mutation rate
    m_bits (int)            : number of bits
    """
    nbits = round(mu * (len(offsprings) * m_bits * 2))
    for i in range(nbits):
        offspring = random.randint(0, len(offsprings) - 1)
        bit = random.randint(0, m_bits * 2 - 1)
        # flip bits
        if offsprings[offspring][bit] == 1:
            offsprings[offspring][bit] = 0
        else:
            offsprings[offspring][bit] = 1

    return offsprings

def update_population(f, current_population, offsprings, keep, x_range, y_range, m_bits):
    """Update population

    f (function)                : cost function
    current_population (list)   : current population
    offsprings (list)           : offsprings
    keep (int)                  : number of population to keep
    x_range (list)              : range of x
    y_range (list)              : range of y
    m_bits (int)                : number of bits
    """
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

M_BITS = 4
N_POP = 4
N_KEEP = 2
MUTATE_RATE = 0.1
# max number of generations
MAX_GEN = 10000
# crossover points
crossover = [3, 6]

# cost function to minimize
def f(x, y): return -x * ((y / 2) - 10)
# bounds
x_range = [10, 20]
y_range = [-5, 7]

current_population = generate_population(f, N_POP, x_range, y_range, M_BITS)
print_as_table(current_population)
#   n  encoding                  decoded x, y       cost
# ---  ------------------------  --------------  -------
#   0  [0, 0, 0, 0, 1, 1, 1, 0]  [10.0, 6.2]      69.000
#   1  [0, 1, 0, 0, 0, 0, 1, 0]  [12.67, -3.4]   148.240
#   2  [0, 1, 1, 0, 0, 1, 0, 0]  [14.0, -1.8]    152.600
#   3  [1, 1, 1, 1, 0, 0, 0, 1]  [20.0, -4.2]    242.000

for i in range(MAX_GEN):
    # generate offsprings
    offsprings = generate_offsprings(current_population, crossover)
    # mutate
    offsprings = mutate(offsprings, MUTATE_RATE, M_BITS)
    # update population
    current_population = update_population(
        f,
        current_population,
        offsprings,
        N_KEEP,
        x_range,
        y_range,
        M_BITS
    )

print_as_table(current_population)
#   n  encoding                  decoded x, y      cost
# ---  ------------------------  --------------  ------
#   0  [0, 0, 0, 0, 1, 1, 1, 1]  [10.0, 7.0]     65.000
#   1  [0, 0, 0, 0, 1, 1, 1, 1]  [10.0, 7.0]     65.000
#   2  [0, 0, 0, 0, 1, 1, 1, 1]  [10.0, 7.0]     65.000
#   3  [0, 0, 0, 0, 1, 1, 1, 1]  [10.0, 7.0]     65.000
