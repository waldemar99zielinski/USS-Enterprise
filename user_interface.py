# For user interface implementation


# number_of_crewmates           -   number of crewmates
# population_size               -   number of specimens for the evolutionary algorithm
# population_generation_mode    -   if "random", crewmate values generated randomly. Otherwise holds filename.
# maximum_crewmate_cost         -   upper bound on integer value of any given crewmate
# rng_seed                      -   if "default", do not provide a seed. Otherwise holds provided seed.
# mutation_range                -   how drastic is the mutation - number of pair swaps performed
# generation_limit              -   how many generations of evolution to perform
class UserParameters:

    def __init__(self):

        self.number_of_crewmates = 1
        self.population_size = 1
        self.population_generation_mode = "random"
        self.maximum_crewmate_cost = 1
        self.rng_seed = "default"
        self.mutation_range = 1
        self.generation_limit = 100


# reads user parameters
def take_user_parameters():
    staging = UserParameters()
    while True:
        try:
            staging.number_of_crewmates = int(input("Enter number of crewmates: "))
            break
        except ValueError:
            print("Please enter a positive integer: ")

    while True:
        try:
            staging.population_size = int(input("Enter population size for the evolutionary algorithm: "))
            break
        except ValueError:
            print("Please enter a positive integer: ")

    staging.population_generation_mode = input("Enter    random    to generate crewmates randomly, or enter a filename to read crewmate values from file: ")

    while True:
        try:
            staging.maximum_crewmate_cost = int(input("Enter maximum crewmate cost: "))
            break
        except ValueError:
            print("Please enter a positive integer: ")

    staging.rng_seed = input("Do you want to provide your own seed for the random number generator (y/n): ")
    if staging.rng_seed == "n":
        staging.rng_seed = "default"
    else:
        while True:
            try:
                staging.rng_seed = int(input("Enter seed: "))
                break
            except ValueError:
                print("Please enter a positive integer: ")


    while True:
        try:
            staging.mutation_range = int(input("Enter mutation severity: "))
            break
        except ValueError:
            print("Please enter a positive integer: ")


    while True:
        try:
            staging.generation_limit = int(input("Enter generation limit: "))
            break
        except ValueError:
            print("Please enter a positive integer: ")


    return staging


# display results and percent comparison
# sjf_solution              -   object of type SolutionInstance, returned by sjf
# evolution_solution        -   expects fitness_log returned by evolutionary algorithm
def display_results(sjf_solution, evolution_solution):
    sjf_value = sjf_solution.fitness
    last_pop = evolution_solution[-1]
    last_pop.sort()
    evo_value = last_pop[-1]
    solution_ratio = (((evo_value/sjf_value)-1)*100)
    print("Service time of SJF result:", end=" ")
    print(sjf_value)
    print("Service time of evolutionary result:", end=" ")
    print(evo_value)
    print("Evolutionary result time is", end=" ")
    print(solution_ratio, end='')
    print("% longer than SJF result.")
