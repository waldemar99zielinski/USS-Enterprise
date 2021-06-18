# evolution draft
from randomization import *
from evolution_selection import *
from evolution_crossover import *
from evolution_mutation import *
from evolution_replacement import *
from generate_intial_population import *
from randomization import  *
from solution_data import getSolutionsListFitness
from population_comparison import are_populations_the_same
from plots import *
from evolution import *
from datetime import datetime
from SJF import *
from user_interface import display_results

#initialize_rng(5) #190
crewmates_number_values = [10, 20, 50, 100, 500, 1000, 5000, 10000]
sjf_time_file = open("sjf_time.txt", "a")
evo_time_file = open("evo_time.txt", "a")
res_diff_file = open("res_diff.txt", "a")
for number in crewmates_number_values:
    initialize_rng(112996)
    init_pop = generate_init_population(100, number, 1000, 3)

    start_time = datetime.now()
    sjf_log = shortest_job_first(SolutionInstance(init_pop[0].order))
    end_time = datetime.now()

    sjf_time = end_time - start_time
    sjf_time_file.write(str(sjf_time))

    start_time = datetime.now()
    evo_log = evolutionary_algorithm_stop(init_pop, 100, 100, 0.5, 20)
    end_time = datetime.now()

    evo_time = end_time - start_time
    evo_time_file.write(str(evo_time))

    print("log len",len(evo_log))
    print("time diff: ",sjf_time, evo_time)
    res_diff_file.write(str(display_results(sjf_log, evo_log)))

# get_fitness_scatter_plot(evo_log)
# get_fitness_average_scatter_plot(evo_log)

# print(shortest_job_first(init_pop[0]))