from solution_data import *
from randomization import *
from SJF import *
from random_generation import *
from evolution_mutation import *
from evolution_replacement import *
from randomization import *
from user_interface import *
from file_access import *
from generate_intial_population import *
from evolution import *


user_params = take_user_parameters()

if user_params.rng_seed == "default":
    initialize_rng()
else:
    initialize_rng(user_params.rng_seed)

print("")
print("")
print("------------------------------------------------------------------")

percentage_results = []

for x in range(10):
    print("Test number:", end=" ")
    print(x+1)

    if user_params.population_generation_mode != "random":
        list_from_file = read_crewmates_from_file(user_params.population_generation_mode)
        progenitor = SolutionInstance(list_from_file)
        starting_population = generate_population_from_progenitor(user_params.population_size, user_params.number_of_crewmates, user_params.maximum_crewmate_cost, user_params.number_of_crewmates, progenitor)
    else:
        starting_population = generate_init_population(user_params.population_size, user_params.number_of_crewmates, user_params.maximum_crewmate_cost, user_params.number_of_crewmates)
        progenitor = SolutionInstance(starting_population[0].order)

    print("SJF started")
    SJF_result = shortest_job_first(progenitor)

    print("Evolutionary algorithm started")
    EVO_result = evolutionary_algorithm(starting_population, user_params.generation_limit, user_params.kids_per_generation, user_params.crossover_probability, user_params.mutation_range)

    print("Finished. Results:")
    percentage_results.append(display_results(SJF_result, EVO_result))
    print("------------------------------------------------------------------")

print("Average quality:", end=" ")
print(sum(percentage_results)/len(percentage_results), end="")
print("%")
