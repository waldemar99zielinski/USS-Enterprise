from random_generation import *
from solution_data import *
from evolution_mutation import *
from randomization import *


# returns population of solutions that consists number_of_species, each with number_of_crewmates
# max_cost defines maximum time to serve a crewmate
# allows multiple species with same order
def generate_init_population(number_of_species, number_of_crewmates, max_cost, mutation_range):
    initial_population = []
    init_species = SolutionInstance(generate_crewmates(number_of_crewmates, max_cost))
    for _ in range(number_of_species):
        species = SolutionInstance(mutate(init_species, mutation_range).order)
        initial_population.append(species)
        # #species.calculate_fitness
        # print(species.order, species.fitness, id(species))
    return initial_population


# init_pop = generate_init_population(10, 10, 100, 2)
# for s in init_pop:
#     print(s.order, s.fitness)