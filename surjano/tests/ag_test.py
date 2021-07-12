#!/bin/python3
import sys 
sys.path.append('..')

import unittest
from src.controllers.ag import Ag 
from src.controllers.rotated_ellipsoide import RotatedEllipsoid 

from src.factory.rotated_factory import RotatedEllipsoidFactory


class AgTest(unittest.TestCase):

    #Retornar uma lista OK 
    #Deve conter uma quantidade de individuos definada por parametros OK
    #Chromosomos aleatorios 
    #Os individuos sao objetos
    def test_initial_population_list(self):
        ag = Ag()
        population = ag.initial_population(RotatedEllipsoidFactory,40)
    
    def test_mutation(self):
        ag = Ag()
        ag.initial_population(RotatedEllipsoidFactory,5)
        mutants = ag.get_mutations(RotatedEllipsoidFactory)
        self.assertIsInstance(mutants[0], (RotatedEllipsoid,list, float))
    
    
if __name__ == "__main__":
    unittest.main()