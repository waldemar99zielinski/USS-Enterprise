from random_generation import *
from solution_data import *
from evolution_mutation import *
from randomization import *

# returns population of solutions that consists number_of_species, each with number_of_crewmates
# max_cost defines maximum time to serve a crewmate
# allows multiple species with same order
def generate_initial_population(number_of_species, number_of_crewmates, max_cost, mutation_range):
    initial_population = []
    init_specie = SolutionInstance(generate_crewmates(number_of_crewmates, max_cost))
    for _ in range(number_of_species):
        specie = mutate(init_specie, mutation_range)
        initial_population.append(specie)
        print(specie.order)
    return initial_population

