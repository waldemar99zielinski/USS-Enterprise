import solution_data

test = solution_data()
test.order = [4, 2, 6]

test.fitness = calculate_fitness(test)

print(test.fitness)