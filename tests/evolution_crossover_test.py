import unittest
from evolution_crossover import *
from solution_data import *
from randomization import *

class CrossoverTest(unittest.TestCase):



    def test1(self):
        initialize_rng(22)

        order1a = [5, 6, 1, 12, 7, 8, 15]
        order1b = [15, 6, 12, 1, 8, 7, 5]
        solution1a = SolutionInstance(order1a)
        solution1b = SolutionInstance(order1b)

        crossed_solution = order_crossover(solution1a, solution1b)
        self.assertEqual(crossed_solution.order, [5, 6, 15, 12, 1, 8, 7])

    def test2(self):
        initialize_rng(11)

        order1a = [5, 6, 1, 12, 7, 8, 15]
        order1b = [15, 6, 12, 1, 8, 7, 5]
        solution1a = SolutionInstance(order1a)
        solution1b = SolutionInstance(order1b)

        crossed_solution = order_crossover(solution1a, solution1b)

        self.assertEqual(crossed_solution.order, [5, 6, 1, 12, 15, 8, 7])