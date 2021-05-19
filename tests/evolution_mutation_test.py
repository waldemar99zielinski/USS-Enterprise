import unittest
from solution_data import *
from randomization import *
from evolution_mutation import *


class MutationTest(unittest.TestCase):

    def test1(self):
        initialize_rng(1255)

        order1a = [5, 6, 1, 12, 7, 8, 15]

        solution1a = SolutionInstance(order1a)


        mutation = mutate(solution1a, 1)

        self.assertEqual(mutation.order, [5, 6, 12, 1, 7, 8, 15])

    def test2(self):
        initialize_rng(1255)

        order1a = [5, 6, 1, 12, 7, 8, 15]
        # 6, 1, 12, 5, 7, 8, 15
        solution1a = SolutionInstance(order1a)

        mutation = mutate(solution1a, 3)

        self.assertEqual(mutation.order, [6, 1, 12, 5, 7, 8, 15])
