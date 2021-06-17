from solution_data import sort_solutions


def are_populations_the_same(p1, p2):
    population1 = sort_solutions(p1)
    population2 = sort_solutions(p2)

    for i in range(len(population1)):
        if population1[i].order != population2[i].order:
            return False
    return True
