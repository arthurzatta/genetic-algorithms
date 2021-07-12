#!/bin/python3
import unittest
import sys
sys.path.append('..')

from src.controllers.rotated_ellipsoid import RotatedEllipsoid
from src.factory.rotated_factory import RotatedEllipsoidFactory

class SurjanoTest(unittest.TestCase):

    def test_crossover(self):
        surjano = RotatedEllipsoidFactory.factory([2,3])
        self.assertEqual(surjano.crossover([3,1]), [[2.33, 2.324], [2.67, 1.66]])

    def test_blx_alfa(self):
        surjano = RotatedEllipsoid([2,3])
        self.assertIsNot(surjano.blx_alfa([3,1]), [0,0])

    def test_mutation(self):
        surjano = RotatedEllipsoid([2,3])
        mutant = surjano.mutate()
        self.assertEqual(mutant, [0,0], "This is not the best value")

    def test_evaluate(self):
        surjano = RotatedEllipsoid([0,0])
        fitness = surjano.evaluate()
        self.assertEqual(fitness, 0)

    
if __name__ == "__main__":
    unittest.main()