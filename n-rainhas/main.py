from ag import Ag
from nRainhasFactory import RainhasFactory 

POPULATION_SIZE = 20 
MAX_GENERATIONS = 100
ELITISM = 8
MAX = False

ag = Ag()
sons = ag.executar(MAX_GENERATIONS, POPULATION_SIZE, ELITISM, MAX)

