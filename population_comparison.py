from solution_data import sort_solutions


def are_populations_the_same(p1, p2):
    population1 = sort_solutions(p1)
    population2 = sort_solutions(p2)
    print("population1")
    for x in population1:
        print(x.order)
    print("population2")
    for x in population2:
        print(x.order)
    for i in range(len(population1)):
        print("population1")
        print( population1[i].order)
        print("population2")
        print(population2[i].order)
        print(population1[i].order == population2[i].order)
        if population1[i].order != population2[i].order:
            return False
    return True
