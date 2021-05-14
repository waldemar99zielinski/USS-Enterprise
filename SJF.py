from solution_data import *

# expects a single object of type solution_instance
# sorts its order field and calculates fitness
def shortest_job_first(source):
    source.order.sort()
    source.fitness = calculate_fitness(source)
