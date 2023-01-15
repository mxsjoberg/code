import random

MAX_ITERATIONS = 50

random.seed(1234)

def generate_swarm(x_0, n_par):
    dimensions = len(x_0)
    swarm = []
    # generate particles
    for i in range(0, n_par):        
        # particle positions
        position = []
        # best position
        position_best = -1
        # particle velocity
        velocity = []
        # particle error
        error = -1
        # best
        error_best = error
        for i in range(0, dimensions):
            velocity.append(random.uniform(-1, 1))
            position.append(x_0[i])
        # append particle
        swarm.append([dimensions, position, position_best, velocity, error, error_best])

    return swarm

def update_velocity(velocity, position, position_best, global_pos):
    # constant inertia weight
    weight = 0.5
    # cognative constant
    c_1 = 1
    # social constant
    c_2 = 2
    # random bias
    r_1 = random.random()
    r_2 = random.random()
    # update velocity
    velocity_cognative = c_1 * r_1 * (position_best - position)
    velocity_social = c_2 * r_2 * (global_pos - position)
    velocity = weight * velocity + velocity_cognative + velocity_social
    
    return velocity

def update_position(position, velocity):
    position = position + velocity
    
    return position

# TODO: clean this up! maybe dict for readability?
def iterate_swarm(f, swarm, bounds=None, global_best=-1, global_pos=-1):
    dimensions = swarm[0][0]
    # iterate particles and evaluate cost function
    for j in range(0, len(swarm)):
        position = swarm[j][1]
        # position_best = swarm[j][2]
        # velocity = swarm[j][3]
        error = f(position)
        error_best = swarm[j][5]
        # update individual best if current position is best
        if (error < error_best or error_best == -1):
            swarm[j][2] = position
            swarm[j][5] = error
        # update error
        swarm[j][4] = error
        # 
        position_best = swarm[j][2]
        velocity = swarm[j][3]
        # update global best if current particle is best
        if (error < global_best or global_best == -1):
            global_pos = list(position)
            global_best = float(error)
        for i in range(0, dimensions):
            velocity[i] = update_velocity(velocity[i], position[i], position_best[i], global_pos[i])
            # velocity[i] = update_velocity(velocity[i], position[i])
            position[i] = update_position(position[i], velocity[i])
            # check bounds
            if bounds:
                # maximum position
                if (position[i] > bounds[i][1]):
                    position[i] = bounds[i][1]
                # minimum position
                if (position[i] < bounds[i][0]):
                    position[i] = bounds[i][0]
    # return
    return swarm, global_best, global_pos

# # minimize x^5 - 3x^4 + 5 over [0, 4]
# # note that x: [x_1, x_2, ..., x_n]
# def f(x):
#     return x[0] ** 5 - 3 * x[0] ** 4 + 5

# global_best = -1
# global_pos = -1
# swarm = generate_swarm(x_0=[5], n_par=15)
# for i in range(MAX_ITERATIONS):
#     swarm, global_best, global_pos = iterate_swarm(f, swarm, bounds=[(0, 4)], global_best=global_best, global_pos=global_pos)
# print((global_best, global_pos))
# # (-14.906559999999999, [2.40000001686553])

# assert (global_best, global_pos) == (-14.906559999999999, [2.40000001686553])

# minimize -(5 + 3x - 4y - x^2 + x y - y^2)
def f(x):
    return -(5 + 3 * x[0] - 4 * x[1] - x[0] ** 2 + x[0] * x[1] - x[1] ** 2)

global_best = -1
global_pos = -1
swarm = generate_swarm(x_0=[5, 5], n_par=15)
for i in range(MAX_ITERATIONS):
    swarm, global_best, global_pos = iterate_swarm(f, swarm, global_best=global_best, global_pos=global_pos)
print((global_best, global_pos))
# (-9.333333333218729, [0.6666736996356956, -1.666654346375958])

# assert (global_best, global_pos) == (-9.333333329790616, [0.6667345761501654, -1.6666235499265152])


