from randomization import *


# expects a single object of type SolutionInstance
# if specimen.order has at least 2 elements, the function chooses 2 randomly and swaps their places
# mutation_range: how many swaps in order
def mutate(specimen, mutation_range):
    size = len(specimen.order)
    if size < 2:
        return specimen
    for _ in range(mutation_range):
        positions = select_from_list(range(0, size-1), 2)
        #print("positions: ", positions)
        specimen.order[positions[0]], specimen.order[positions[1]] = specimen.order[positions[1]], specimen.order[positions[0]]
    return specimen
