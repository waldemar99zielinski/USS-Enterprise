# For implementing crossover
# 1. function for crossover: takes two solution_instance
from randomization import *
from solution_data import *


# takes array of 2 solutions and returns solution with their crossed genome order
def order_crossover(solutions):
    solution_instance1 = solutions[0]
    solution_instance2 = solutions[1]
    # order for each solution has the same length
    matching_section_index = generate_random_from_range(len(solution_instance1.order))
    # unchanged part of solution
    crossed_solution_order = solution_instance1.order[:matching_section_index]

    missing_solution_part_order = []
    for s in range(matching_section_index, len(solution_instance1.order)):
        index = solution_instance2.order.index(solution_instance1.order[s])

        # populate array with pair index, time
        missing_solution_part_order.append((index, solution_instance1.order[s]))

    missing_solution_part_order.sort()

    # crossed part of the solution
    for s in missing_solution_part_order:
        # append missing values to final crossover solution
        crossed_solution_order.append(s[1])

    return SolutionInstance(crossed_solution_order)
