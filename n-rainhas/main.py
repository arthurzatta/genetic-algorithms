from ag import Ag

POPULATION_SIZE = 40 
MAX_GENERATIONS = 200
ELITISM = 8
MAX = False

ag = Ag()
sons = ag.execute(MAX_GENERATIONS, POPULATION_SIZE, ELITISM, MAX)

