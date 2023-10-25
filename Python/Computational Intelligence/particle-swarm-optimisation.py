# PSO is a population-based stochastic optimization technique
# inspired by social behavior of bird flocking or fish schooling.
# It is used to find an optimal solution to a problem by
# iteratively moving particles through the solution space.

import random

# constant inertia weight
weight = 0.5
# cognative constant
c_1 = 1
# social constant
c_2 = 2

def generate_swarm(x_0, n_par):
    """Generate swarm of particles

    x_0 (list)              : initial position
    n_par (int)             : number of particles
    """

    dimensions = len(x_0)
    swarm = []
    # generate particles
    for i in range(0, n_par):
        position = []
        # best position
        position_best = -1
        # particle velocity
        velocity = []
        # particle error (cost)
        error = -1
        # best error (cost)
        error_best = error
        # position and velocity
        for i in range(0, dimensions):
            position.append(x_0[i])
            velocity.append(random.uniform(-1, 1))
        # append particle
        swarm.append({
            "dimensions": dimensions,
            "position": position,
            "position_best": position_best,
            "velocity": velocity,
            "error": error,
            "error_best": error_best
        })

    return swarm

def update_velocity(velocity, position, position_best, global_pos):
    """Update particle velocity
    
    velocity (float)        : particle velocity
    position (float)        : particle position
    position_best (float)   : best position
    global_pos (float)      : global best position
    """

    # random bias
    r_1 = random.random()
    r_2 = random.random()
    # update velocity
    velocity_cognative = c_1 * r_1 * (position_best - position)
    velocity_social = c_2 * r_2 * (global_pos - position)
    velocity = weight * velocity + velocity_cognative + velocity_social
    
    return velocity

def update_position(position, velocity):
    """Update particle position
    
    position (float)        : particle position
    velocity (float)        : particle velocity
    """

    position = position + velocity
    return position

def iterate_swarm(f, swarm, bounds=None, global_best=-1, global_pos=-1):
    """Iterate swarm
    
    f (function)            : cost function
    swarm (list)            : list of particles
    bounds (list)           : list of bounds for each dimension
    global_best (float)     : global best error
    global_pos (float)      : global best position
    """

    # iterate particles and evaluate cost function
    for j in range(0, len(swarm)):
        dimensions = swarm[j]["dimensions"]
        position = swarm[j]["position"]
        error_best = swarm[j]["error_best"]
        # evaluate new error (cost)
        error = swarm[j]["error"] = f(position)
        # update local best position if current position gives
        # better local error
        if (error < error_best or error_best == -1):
            swarm[j]["position_best"] = position
            swarm[j]["error_best"] = error
        position_best = swarm[j]["position_best"]
        velocity = swarm[j]["velocity"]
        # update global best if position of current particle gives
        # best global error
        if (error < global_best or global_best == -1):
            global_pos = list(position)
            global_best = float(error)
        # update particle velocity and position
        for i in range(0, dimensions):
            velocity[i] = update_velocity(
                velocity[i],
                position[i],
                position_best[i],
                global_pos[i]
            )
            position[i] = update_position(
                position[i],
                velocity[i]
            )
            # max value for position
            if bounds and (position[i] > bounds[i][1]):
                position[i] = bounds[i][1]
            # min value for position
            if bounds and (position[i] < bounds[i][0]):
                position[i] = bounds[i][0]
    # return
    return swarm, round(global_best, 2), [round(pos, 2) for pos in global_pos]

MAX_ITERATIONS = 50
random.seed(42)

# minimize x^5 - 3x^4 + 5 over [0, 4]
def f(x): return x[0] ** 5 - 3 * x[0] ** 4 + 5
# reset global
global_best = -1
global_pos = -1
# initial swarm
swarm = generate_swarm(x_0=[5], n_par=15)
# iterate swarm
for i in range(MAX_ITERATIONS):
    swarm, global_best, global_pos = iterate_swarm(
        f,
        swarm,
        bounds=[(0, 4)],
        global_best=global_best,
        global_pos=global_pos
    )
assert (global_best, global_pos) == (-14.91, [2.39])

# minimize -(5 + 3x - 4y - x^2 + x y - y^2)
def f(x): return -(5 + 3 * x[0] - 4 * x[1] - x[0] ** 2 + x[0] * x[1] - x[1] ** 2)
# reset global
global_best = -1
global_pos = -1
# initial swarm
swarm = generate_swarm(x_0=[5, 5], n_par=15)
# iterate swarm
for i in range(MAX_ITERATIONS):
    swarm, global_best, global_pos = iterate_swarm(
        f,
        swarm,
        global_best=global_best,
        global_pos=global_pos
    )
assert (global_best, global_pos) == (-9.33, [0.67, -1.67])
