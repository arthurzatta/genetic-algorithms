from functools import reduce
import random
import math
from abc import ABC, abstractmethod 

class Surjano(ABC):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = 0.0
        self.evaluated = False

    #Arithmetic crossover
    def crossover(self, parent, alfa=0.33):
        son1 = []
        son2 = []
        for i in range(len(self.chromosome)):
            son1.append((1-alfa) * self.chromosome[i] + alfa * parent[i])
            son2.append((1-alfa) * parent[i] + alfa * self.chromosome[i])           
        return [son1,son2]

    #Blx-alfa racombination
    def blx_alfa(self,parent):
        son1 = []
        son2 = []
        for i in range(len(self.chromosome)):
            alfa = random.gauss(mu=0, sigma=0.1)   
            
            distance = abs(self.chromosome[i] - parent[i])

            son1.append(self.chromosome[i] + alfa * distance)
            son2.append(parent[i] + alfa * distance)            
        return [son1,son2]

    #Gaussian mutation
    def mutate(self, mutation_rate=0.05):
        mutant = []

        for gene in self.chromosome:
            rand_rate = random.random()
            if rand_rate >= mutation_rate:
                alfa = random.gauss(mu=0, sigma=0.1)   
                mutant.append(gene + alfa)
            else:
                mutant.append(gene)
        if mutant == self.chromosome:
            index = random.randint(0,len(self.chromosome))
            alfa = random.gauss()
            mutant[index] += alfa
        return mutant
        
    #ROTATED HYPER-ELLIPSOID FUNCTION      
    @abstractmethod
    def evaluate(self):
        pass

    def get_evaluate(self):
        if not self.evaluated:
            self.fitness = self.evaluate()
            self.evaluate = True
            return self.fitness
        else:
            self.fitness