# For implementing evolutionary algorithm

# evolution draft
from randomization import *
from evolution_selection import *
from evolution_crossover import *
from evolution_mutation import *

GENERATIONS = 100

def evolutionary_algorithm(init_population, generations, kids_per_generation,crossover_probability):

    population = init_population
    kids =[]

    for _ in range(generations):
        for _ in range(kids_per_generation):
            child = None

            if crossover_probability < generate_probability():
                child = mutate(order_crossover(selection_tournament(population, 2, 5)),1)
            else:
                child = mutate(selection_tournament(population, 1, 5),1)
            kids.append(child)

        # TODO: replacement strategies
        # population = replacement
