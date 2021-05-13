from solution_data import *
from evolution_crossover import *
# order = [4, 2, 6]
# test = SolutionInstance(order)
# 
# 
# print(test.fitness)

order1 = [2, 4, 9, 21, 41, 7, 4, 2]
solution1 = SolutionInstance(order1)
order2 = [21, 4, 7, 4, 41, 9, 2, 2]
solution2 = SolutionInstance(order2)

order_crossover(solution1, solution2)
