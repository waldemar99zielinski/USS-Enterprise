from randomization import *
from solution_data import *


# Returns a list of most fit specimens
# slots is the number of specimens returned
# does not modify original list
def most_fit(specimens, slots):
    staging = sort_solutions(specimens)
    staging = staging[:slots]
    return staging


# Returns winners of the tournament
# each round has only one winner, determined by fitness
# slots is the number of rounds (and also the number of returned elements)
# specimens is a list of SolutionInstance objects
# bracket_size is the number of specimens selected to compete in a single round
def tournament(specimens, slots, bracket_size):
    results = []
    if (bracket_size > len(specimens)):
        print("Error in tournament - bracket_size must be smaller than the number of specimens")
        return results
    for x in range(slots):
        results.append(sort_solutions(select_from_list(specimens, bracket_size))[0])
    return results
