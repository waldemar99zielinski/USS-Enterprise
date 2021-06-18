# For implementing evolutionary algorithm

# evolution draft
from randomization import *
from evolution_selection import *
from evolution_crossover import *
from evolution_mutation import *
from evolution_replacement import *
from generate_intial_population import *
from randomization import  *
from solution_data import getSolutionsListFitness
from population_comparison import are_populations_the_same


def evolutionary_algorithm(init_population, generation_limit, kids_per_generation, crossover_probability, mutation_range):
    population = init_population
    kids = []
    fitness_log = []
    fitness_log.append(getSolutionsListFitness(init_population))
    for x in range(generation_limit):

        for _ in range(kids_per_generation):
            child = None

            if crossover_probability > generate_probability():

                child = mutate(order_crossover(selection_tournament(population, 2, 5)), mutation_range)
            else:
                child = mutate(selection_tournament(population, 1, 5)[0], mutation_range)
            kids.append(child)


        population = population + kids

        kids = []
        fitness_log.append(getSolutionsListFitness(population))
        #replace population
        population = most_fit(population, len(init_population[0].order))




    return fitness_log


# generation_limit: stop algorithm if no changes in population within generation_limit
def evolutionary_algorithm_stop(init_population, generation_limit, kids_per_generation, crossover_probability, mutation_range):
    population = init_population
    kids = []
    fitness_log = []
    fitness_log.append(getSolutionsListFitness(init_population))
    no_population_changes_counter = 0

    while no_population_changes_counter < generation_limit:
        for _ in range(kids_per_generation):
            child = None

            if crossover_probability > generate_probability():

                child = mutate(order_crossover(selection_tournament(population, 2, 5)), mutation_range)
            else:

                child = mutate(selection_tournament(population, 1, 5)[0], mutation_range)
            kids.append(child)

        new_population = population + kids
        kids = []
        population_to_replace = most_fit(new_population, len(init_population[0].order))

        # check if there were any changes in population
        if are_populations_the_same(population, population_to_replace):
            no_population_changes_counter += 1
        else:
            no_population_changes_counter = 0

        fitness_log.append(getSolutionsListFitness(new_population))
        population = most_fit(new_population, len(init_population[0].order))

    return fitness_log

