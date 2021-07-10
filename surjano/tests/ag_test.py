#!/bin/python3
import sys 
sys.path.append('..')

import unittest
from src.controllers.ag import Ag 
from src.controllers.rotated_ellipsoide import RotatedEllipsoide 

from src.factory.rotated_factory import RotatedEllipsoideFactory


class AgTest(unittest.TestCase):

    #Retornar uma lista OK 
    #Deve conter uma quantidade de individuos definada por parametros OK
    #Chromosomos aleatorios 
    #Os individuos sao objetos
    def test_initial_population_list(self):
        ag = Ag()
        population = ag.initial_population(RotatedEllipsoideFactory,40)
    
    def test_mutation(self):
        ag = Ag()
        ag.initial_population(RotatedEllipsoideFactory,5)
        mutants = ag.get_mutations(RotatedEllipsoideFactory)
        self.assertIsInstance(mutants[0], (RotatedEllipsoide,list, float))
    
    
if __name__ == "__main__":
    unittest.main()