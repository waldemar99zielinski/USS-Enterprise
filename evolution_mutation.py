from randomization import *
from solution_data import *


# expects a single object of type solution_instance
# if specimen.order has at least 2 elements, the function chooses 2 randomly and swaps their places
def mutate(specimen):
    size = len(specimen.order)
    if (size < 2):
        return specimen
    positions = select_from_list(range(0, size-1), 2)
    specimen.order[positions[0]], specimen.order[positions[1]] = specimen.order[positions[1]], specimen.order[positions[0]]
    return specimen
