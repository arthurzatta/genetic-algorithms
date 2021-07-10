#!/bin/python3
import sys 
sys.path.append('..')

import unittest
from src.controllers.dixon import Dixon

class DixonTest(unittest.TestCase):

    def test_dixon(self):
        dixon = Dixon([2,3])
        dixon.evaluate()

        self.assertEqual(dixon.fitness, 50)
if __name__ == "__main__":
    unittest.main()