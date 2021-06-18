from randomization import *


# generates a list of random numbers representing crewmates (time to complete their orders)
# amount specifies how many crewmates to generate
# max_cost specifies the maximum time cost of an individual order (minimum is 1)
def generate_crewmates(amount, max_cost):
    staging = []
    for x in range(amount):
        staging.append(generate_random_from_range(max_cost))
    return staging
