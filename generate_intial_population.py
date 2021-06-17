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
        print("gen_init: ", species.order, species.fitness)
        initial_population.append(species)
        print(initial_population[_].order, initial_population[_].fitness)

    for x in initial_population:
        print("finale ", x.order, x.fitness)
    return initial_population


# returns population of solutions that consists number_of_species, each with number_of_crewmates
# max_cost defines maximum time to serve a crewmate
# allows multiple species with same order
# population consists of progenitor and his mutants
def generate_population_from_progenitor(number_of_species, number_of_crewmates, max_cost, mutation_range, progenitor):
    initial_population = []
    init_species = progenitor
    initial_population.append(init_species)
    for _ in range(number_of_species-1):
        species = SolutionInstance(mutate(init_species, mutation_range).order)
        initial_population.append(species)
    return initial_population