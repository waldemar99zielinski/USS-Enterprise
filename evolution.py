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
from plots import *
from SJF import shortest_job_first



def evolutionary_algorithm(init_population, generation_limit, kids_per_generation, crossover_probability, mutation_range):


    population = init_population
    kids = []
    fitness_log = []
    fitness_log.append(getSolutionsListFitness(init_population))
    for x in range(generation_limit):
        # print("GENERATION: ", x)
        for _ in range(kids_per_generation):
            child = None

            if crossover_probability > generate_probability():
                child = mutate(order_crossover(selection_tournament(population, 2, 5)), mutation_range)
            else:
                child = mutate(selection_tournament(population, 1, 5)[0], mutation_range)
            kids.append(child)
        population = population + kids
        kids = []
        population = most_fit(population, len(init_population[0].order))
        fitness_log.append(getSolutionsListFitness(population))

        # for s in population:
        #     print(s.order, s.fitness)

    return fitness_log


# move later
# -------------------------------------------------------------------------------

#initialize_rng(5) #190
#initialize_rng(555)
#init_pop = generate_init_population(10, 100, 100, 5)



# for s in init_pop:
#     print(s.order, s.fitness)
#log = evolutionary_algorithm(init_pop, 1000, 100, 0.5, 2)

#print(len(log),log)

# get_fitness_scatter_plot(log)
#get_fitness_average_scatter_plot(log)

#print(shortest_job_first(init_pop[0]))