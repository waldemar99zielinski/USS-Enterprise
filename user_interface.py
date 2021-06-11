# For user interface implementation


# number_of_crewmates           -   number of crewmates
# population_size               -   number of specimens for the evolutionary algorithm
# population_generation_mode    -   if "random", crewmate values generated randomly. Otherwise holds filename.
# maximum_crewmate_cost         -   upper bound on integer value of any given crewmate
# rng_seed                      -   if "default", do not provide a seed. Otherwise holds provided seed.
class UserParameters:

    def __init__(self):

        self.number_of_crewmates = 1
        self.population_size = 1
        self.population_generation_mode = "random"
        self.maximum_crewmate_cost = 1
        self.rng_seed = "default"


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

    return staging

def display_results():
    pass