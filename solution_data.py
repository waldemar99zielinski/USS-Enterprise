# For implementing solution data structures and fitness function
import math

class solution_instance:
    order = []
    fitness = math.inf


def calculate_fitness(solution):
    result = 0
    n = len(solution.order)
    for x in solution.order:
        result += (n*x)
        n = n - 1
    return result
