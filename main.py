from solution_data import *

test = solution_instance()
test.order = [4, 2, 6]

test.fitness = calculate_fitness(test)

print(test.fitness)