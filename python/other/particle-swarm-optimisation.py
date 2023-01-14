import random
import math

# constant inertia weight
weight = 0.5
# cognative constant
c_1 = 1
# social constant
c_2 = 2

def create_swarm(x_0, n_par):
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

def update_velocity(velocity, global_pos, position):
    r_1 = random.random()
    r_2 = random.random()
    # update velocity
    velocity_cognative = c_1 * r_1 * (global_pos - position)
    velocity_social = c_2 * r_2 * (global_pos - position)
    velocity = weight * velocity + velocity_cognative + velocity_social
    
    return velocity

def update_position(position, velocity):
    position = position + velocity
    
    return position

def optimize(f, swarm, bounds, max_iterations, global_best=-1, global_pos=-1):
    for i in range(max_iterations):
        dimensions = swarm[0][0]
        # iterate particles and evaluate cost function
        for j in range(0, len(swarm)):
            position = swarm[j][1]
            position_best = swarm[j][2]
            velocity = swarm[j][3]
            error = f(position)
            error_best = swarm[j][5]
            # update error
            swarm[j][4] = error
            # update individual best if current position is best
            if (error < error_best or error_best == -1):
                swarm[j][2] = position
                swarm[j][5] = error
            # update global best if current particle is best
            if (error < global_best or global_best == -1):
                global_pos = list(position)
                global_best = float(error)
            for i in range(0, dimensions):
                velocity[i] = update_velocity(velocity[i], global_pos[i], position[i])
                position[i] = update_position(position[i], velocity[i])
                # check bounds
                if bounds:
                    # maximum position
                    if (position[i] > bounds[i][1]):
                        position[i] = bounds[i][1]
                    # minimum position
                    if (position[i] < bounds[i][0]):
                        position[i] = bounds[i][0]
        # result (global best)
        result = (round(global_best, 2), [])
        for i in range(0, dimensions):
            # best position (i.e. x-value)
            result[1].append(round(global_pos[i], 2))

    return result

# minimize x^5 - 3x^4 + 5 over [0, 4]
# x: [x_1, x_2, ..., x_n]
def f_1(x): return x[0] ** 5 - 3 * x[0] ** 4 + 5
swarm = create_swarm(x_0=[5], n_par=15)
result = optimize(f_1, swarm, bounds=[(0, 4)], max_iterations=50)
# print(result)
# (-14.91, [2.4])

assert optimize(f_1, create_swarm(x_0=[5], n_par=15), bounds=[(0, 4)], max_iterations=50) == (-14.91, [2.4])

# minimize -(5 + 3x - 4y - x^2 + x y - y^2)
# x: [x_1, x_2, ..., x_n]
def f_2(x): return -(5 + 3 * x[0] - 4 * x[1] - x[0] ** 2 + x[0] * x[1] - x[1] ** 2)
swarm = create_swarm(x_0=[5, 5], n_par=15)
result = optimize(f_2, swarm, bounds=None, max_iterations=50)
# print(result)
# (-9.33, [0.67, -1.67])

assert optimize(f_2, create_swarm(x_0=[5, 5], n_par=15), bounds=None, max_iterations=50) == (-9.33, [0.67, -1.67])


