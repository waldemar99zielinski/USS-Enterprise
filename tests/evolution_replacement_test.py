import unittest
from solution_data import *
from randomization import *
from evolution_replacement import *


class ReplacementTest(unittest.TestCase):

    def test1(self):
        initialize_rng(1255)

        order1a = [5, 6, 1, 12, 7, 8, 15]
        order1b = [15, 6, 12, 1, 8, 7, 5]
        order1c = [12, 6, 15, 1, 5, 7, 8]
        order1d = [1, 8, 12, 15, 7, 6, 5]
        solution1a = SolutionInstance(order1a)
        solution1b = SolutionInstance(order1b)
        solution1c = SolutionInstance(order1c)
        solution1d = SolutionInstance(order1d)
        population = [solution1a, solution1b, solution1c, solution1d]

        self.assertEqual(most_fit(population, 2)[0].fitness, 176)
        self.assertEqual(most_fit(population, 2)[1].fitness, 213)







