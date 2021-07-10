import random
from ..factory.rotated_factory import RotatedEllipsoideFactory
class Ag:
    def __init__(self):
        self.population = []
        self.maximization = False
        self.factory = None
    def initial_population(self, nInd: int, a:int, b:int):
        self.population =  [[random.uniform(a,b) for d in range(dimension)] for i in range(nInd)]

    def execute(self,nGen:int,nInd:int,elitism:int,maximization:bool, factory) -> None:
        self.factory = factory
        self.initial_population(nInd)
        
        self.maximization = maximization
        
        for gen in range(nGen):
            aux_population = []
            
            aux_population.extend(self.population)
            aux_population.extend(self.get_recombinations())
            aux_population.extend(self.get_mutations())        
            

            self.population = aux_population
            elite = self.elitism(elitism)

            self.selection(nInd-elitism)
            self.population.extend(elite)

            self.printer(gen)
     
    def get_recombinations(self) -> list:
        offsprings = []

        for i in range(0,int(len(self.population)/2),2):
            parents = tuple(self.population[i],self.population[i+1])
            sons = parents[0].crossover(parents[1])
            offsprings.extend(sons)
        offsprings = [self.factory.factory(i) for i in offsprings] 
        return offsprings 

    def get_mutations(self) -> list:
        return list(map(lambda individual: self.factory.factory(individual.mutate()), self.population))

    def selection(self, nInd: int):
        selected_genes = []
        total = self.__evaluation_total() 

        for i in range(nInd):
            if self.maximization:
                random_sorted = random.randint(0,total)
            else:
                random_sorted = random.uniform(0,total) 

            value = self.__wheel_rotation(random_sorted)
            selected_genes.append(value)

        self.population = selected_genes

    def __evaluation_total(self):
        total = 0

        for chromosome in self.population:
            if self.maximization: 
                total += chromosome.get_evaluate()
            else:
                total += 1/(chromosome.get_evaluate()+1)
        return total
        
    def __wheel_rotation(self,raffled):
        roulette_sum = 0
        selected = None

        for chromosome in self.population:

            if self.maximization:
                roulette_sum += chromosome.get_evaluate()
            else:
                roulette_sum += 1/(chromosome.get_evaluate()+1)

            if roulette_sum >= raffled:
                selected = chromosome
                break

        return selected

    def elitism(self,elitism:int):

        aux = sorted(self.population,key=lambda individual: individual.chromosome)
        return aux[:elitism]
    

    def printer(self, gen:int):
        best = self.population[0]
        for chromosome in self.population:
            if not self.maximization and chromosome.get_evaluate() <= best.get_evaluate():
                best = chromosome
            elif self.maximization and chromosome.get_evaluate() >= best.get_evaluate():
                best = chromosome
        print('Geração: {} Individuo: {} Avaliação: {}'.format(gen,best.chromosome,best.fitness))
