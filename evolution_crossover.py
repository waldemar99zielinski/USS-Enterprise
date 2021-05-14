# For implementing crossover
# 1. function for crossover: takes two solution_instance
import random


def order_crossover(solution_instance1, solution_instance2):
    random.seed(101)
    # order for each solution has the same length
    matchingSectionIndex = random.randrange(len(solution_instance1.order))
    print("matchingSectionIndex: ", matchingSectionIndex)
    # unchanged part of solution
    crossedSolutionOrder = solution_instance1.order[:matchingSectionIndex]
    print("crossed soluttion part: ", crossedSolutionOrder)
    missingSolutionPartOrder = []
    for s in range(matchingSectionIndex, len(solution_instance1.order)):
        index = solution_instance2.order.index(solution_instance1.order[s])

        # populate array with pair index, time
        missingSolutionPartOrder.append((index, solution_instance1.order[s]))

    pair = [(1, 2)]
    print(missingSolutionPartOrder)
    missingSolutionPartOrder.sort()
    print(missingSolutionPartOrder)

    # crossed part of the solution
    for s in missingSolutionPartOrder:
        # append missing values to final crossover solution
        crossedSolutionOrder.append(s[1])

    print("crossed soluttion part: ", crossedSolutionOrder)
# 2. function for whole population
