# https://en.wikipedia.org/wiki/Particle_swarm_optimization
import random
import math

# ---------------------------------------------------------------------------
#   Particle
# ---------------------------------------------------------------------------
class Particle:
    def __init__(self, x_0, dimensions):
        self.dimensions = dimensions        # number of decision parameters
        self.position = []                  # particle position
        self.position_best = []             # best position
        self.velocity = []                  # particle velocity
        self.error = -1                     # particle error
        self.error_best = -1                # best error

        for i in range(0, self.dimensions):
            self.velocity.append(random.uniform(-1, 1))
            self.position.append(x_0[i])

    # evaluate cost
    def evaluate(self, cost_function):
        self.error = cost_function(self.position)

        #print(self.error)

        # update individual best if current position is best
        if (self.error < self.error_best or self.error_best == -1):
            self.position_best = self.position
            self.error_best = self.error

    # update velocity
    def update_velocity(self, position_best):
        weight = 0.5                        # constant inertia weight
        c_1 = 1                             # cognative constant
        c_2 = 2                             # social constant

        for i in range(0, self.dimensions):
            r_1 = random.random()
            r_2 = random.random()

            velocity_cognative = c_1 * r_1 * (self.position_best[i] - self.position[i])
            velocity_social = c_2 * r_2 * (position_best[i] - self.position[i])

            self.velocity[i] = weight * self.velocity[i] + velocity_cognative + velocity_social

        # print(self.velocity)

    # update particle position (based on velocity)
    def update_position(self, bounds=None):
        for i in range(0, self.dimensions):
            self.position[i] = self.position[i] + self.velocity[i]

            if bounds:
                # maximum position
                if (self.position[i] > bounds[i][1]): self.position[i] = bounds[i][1]
                # minimum position
                if (self.position[i] < bounds[i][0]): self.position[i] = bounds[i][0]

        # print(self.position)

# ---------------------------------------------------------------------------
#   Particle Swarm Optimisation
# ---------------------------------------------------------------------------
class PSO():
    def __init__(self, cost_function, x_0, bounds, num_particles, max_iterations):
        self.dimensions = len(x_0)
        self.cost_function = cost_function
        self.x_0 = x_0
        self.bounds = bounds
        self.num_particles = num_particles
        self.max_iterations = max_iterations

        # optimisation variables
        self.error_best = -1
        self.position_best = []

        # create swarm
        self.swarm = []
        for i in range(0, num_particles):
            self.swarm.append(Particle(x_0, self.dimensions))

    def optimisation(self):
        for i in range(self.max_iterations):
            # iterate particles and evaluate cost function
            for j in range(0, self.num_particles):
                self.swarm[j].evaluate(self.cost_function)

                # update global best if current particle is best
                if (self.swarm[j].error < self.error_best or self.error_best == -1):
                    self.position_best = list(self.swarm[j].position)
                    self.error_best = float(self.swarm[j].error)

            # iterate particles and update velocity and position
            for j in range(0, self.num_particles):
                self.swarm[j].update_velocity(self.position_best)
                self.swarm[j].update_position(self.bounds)

        # result
        result = (round(self.error_best, 2), [])
        for i in range(0, self.dimensions):
            # print('x_{} ='.format(i), round(self.position_best[i], 2))
            result[1].append(round(self.position_best[i], 2))

        return result

if (__name__ == "__PSO__"): main()

# minimize -(5 + 3x - 4y - x^2 + x y - y^2)
def function(x): return -(5 + 3 * x[0] - 4 * x[1] - x[0] ** 2 + x[0] * x[1] - x[1] ** 2)
print(PSO(function, [5, 5], bounds=None, num_particles=15, max_iterations=50).optimisation())
# (-9.33, [0.67, -1.67])

# minimize x^5 - 3x^4 + 5 over [0, 4]
def function(x): return x[0] ** 5 - 3 * x[0] ** 4 + 5
print(PSO(function, [5], bounds=[(0, 4)], num_particles=15, max_iterations=50).optimisation())
# (-14.91, [2.4])