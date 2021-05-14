from solution_data import *
from randomization import *
from SJF import *
from random_generation import *
from evolution_mutation import *
from evolution_replacement import *

seed = initialize_rng()

x1 = solution_instance()
x2 = solution_instance()
x3 = solution_instance()
x4 = solution_instance()
x5 = solution_instance()


x1.fitness = 1
x2.fitness = 2
x3.fitness = 3
x4.fitness = 4
x5.fitness = 5


test = [x4, x3, x1, x5, x2]

test2 = tournament(test, 3, 2)


for x in range(len(test2)):
    print(test2[x].fitness)


