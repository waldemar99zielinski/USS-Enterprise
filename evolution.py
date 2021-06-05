# For implementing evolutionary algorithm

# evolution draft
from randomization import *
from evolution_selection import *
from evolution_crossover import *
from evolution_mutation import *
from evolution_replacement import *
from generate_intial_population import *
from randomization import  *
GENERATIONS = 100

def evolutionary_algorithm(init_population, generations, kids_per_generation,crossover_probability):

    population = init_population
    kids =[]

    for x in range(generations):
        print("GENERATION: ", x)
        for _ in range(kids_per_generation):
            child = None

            if crossover_probability > generate_probability():
                child = mutate(order_crossover(selection_tournament(population, 2, 5)), 1)
            else:
                child = mutate(selection_tournament(population, 1, 5)[0], 1)
            kids.append(child)
        population = population + kids
        kids=[]
        population = most_fit(population, len(init_population[0].order))
        for s in population:
            print(s.order, s.fitness)

# initialize_rng(5)
# init_pop = generate_init_population(10, 10, 100, 5)
# for s in init_pop:
#     print(s.order, s.fitness)
# evolutionary_algorithm(init_pop, 1000, 5, 0.5)