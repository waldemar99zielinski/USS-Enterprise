import math


class SolutionInstance:

    def __init__(self, order):

        self.order = order
        self.fitness = self.calculate_fitness(self.order)

    def calculate_fitness(self, order):
        result = 0
        n = len(self.order)
        for x in self.order:
            result += (n*x)
            n = n - 1
        return result
