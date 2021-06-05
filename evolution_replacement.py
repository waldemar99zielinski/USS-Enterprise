from randomization import *
from solution_data import *


# Returns a list of most fit specimens
# slots is the number of specimens returned
# does not modify original list
def most_fit(specimens, slots):
    staging = sort_solutions(specimens)
    staging = staging[:slots]
    return staging
