# For implementing evolutionary algorithm

# evolution draft

GENERATIONS = 100
def evolutionary_algorithm(init_population, generations):

    population = init_population

    for _ in range(generations):
        for x in population:
            child = None
            #TODO: think of a condition
            if True:
                # child = mutation X crossover X selection
            else:
                # child = mutation X selection
            population.append(child)
            
            #population = replacement
