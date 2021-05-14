import math


# order is a list of crewmates, represented by the time it takes to complete their order
# fitness is the total wait time (time from start to completion of first order + time from start to completion of second order + ...)
class solution_instance:
    order = []
    fitness = math.inf


# expects a single object of type solution_instance
# calculates and returns its fitness (does not modify object)
def calculate_fitness(solution):
    result = 0
    n = len(solution.order)
    for x in solution.order:
        result += (n*x)
        n = n - 1
    return result


# internal use
def sorting_function(element):
    return element.fitness


# sorts by fitness (ascending)
# does not modify original list
def sort_solutions(source):
    staging = source.copy()
    staging.sort(key=sorting_function)
    return staging
