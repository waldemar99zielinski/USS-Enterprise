import unittest
from solution_data import *
from population_comparison import *


class ReplacementTest(unittest.TestCase):


    def test_same_population(self):
        order1a = [5, 6, 1, 12, 7, 8, 15]
        order1a2 = [5, 6, 1, 12, 7, 8, 15]
        order1b = [15, 6, 12, 1, 8, 7, 5]
        order1c = [12, 6, 15, 1, 5, 7, 8]
        order1d = [1, 8, 12, 15, 7, 6, 5]

        solution1a = SolutionInstance(order1a)
        solution1a2 = SolutionInstance(order1a2)
        solution1b = SolutionInstance(order1b)
        solution1c = SolutionInstance(order1c)
        solution1d = SolutionInstance(order1d)

        population = [solution1a, solution1b, solution1c, solution1d]
        population2 = [solution1a, solution1b, solution1c, solution1d]

        self.assertEqual(are_populations_the_same(population, population2), True)

    def test_diffrent_population(self):
        order1a = [5, 6, 1, 12, 7, 8, 15]
        order1a2 = [5, 6, 1, 12, 7, 8, 15]
        order1b = [15, 6, 12, 1, 8, 7, 5]
        order1c = [12, 6, 15, 1, 5, 7, 8]
        order1d = [1, 8, 12, 15, 7, 6, 5]

        solution1a = SolutionInstance(order1a)
        solution1a2 = SolutionInstance(order1a2)
        solution1b = SolutionInstance(order1b)
        solution1c = SolutionInstance(order1c)
        solution1d = SolutionInstance(order1d)

        population = [solution1a, solution1b, solution1c, solution1d]
        population3 = [solution1b, solution1a2, solution1c, solution1b]

        self.assertEqual(are_populations_the_same(population, population3), False)

    def test_same_genom(self):
        order1a = [5, 6, 1, 12, 7, 8, 15]
        order1a2 = [5, 6, 1, 12, 7, 8, 15]
        order1b = [15, 6, 12, 1, 8, 7, 5]
        order1c = [12, 6, 15, 1, 5, 7, 8]
        order1d = [1, 8, 12, 15, 7, 6, 5]

        solution1a = SolutionInstance(order1a)
        solution1a2 = SolutionInstance(order1a2)
        solution1b = SolutionInstance(order1b)
        solution1c = SolutionInstance(order1c)
        solution1d = SolutionInstance(order1d)

        population = [solution1a, solution1b, solution1c, solution1d]
        population3 = [solution1a2, solution1b, solution1c, solution1d]

        self.assertEqual(are_populations_the_same(population, population3), True)







