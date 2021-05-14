from solution_data import *

# expects a single object of type SolutionInstance
# sorts its order field and calculates fitness
def shortest_job_first(source):
    source.order.sort()
    source.fitness = source.calculate_fitness()

