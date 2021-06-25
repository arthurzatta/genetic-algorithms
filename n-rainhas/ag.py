from nRainhasFactory import RainhasFactory as factory 
import random

class Ag:
    def __init__(self):
        self.population = []
        self.maximization = False
    
    def initial_population(self, nInd: int):
        for individuo in range(nInd):
            auxGene = random.sample(list(range(8)), k=8)
            self.population.append(factory.rainhasFactory(auxGene))

    def executar(self,nGen:int,nInd:int,elitism:int,maximization:bool):
        self.maximization = maximization
        self.initial_population(nInd)
        for gen in range(nGen):
            aux_population = []
            aux_population.extend(self.population)
            aux_population.extend(self.get_filhos())
            aux_population.extend(self.get_mutations())        

            self.population = aux_population
            elite = self.elitism(elitism)

            self.selection(nInd-elitism)
            self.population.extend(elite)

            self.population = random.sample(self.population,k=nInd)
            self.printer(gen)

   #Maybe can be made better
    def get_filhos(self):
        parents = self.population.copy()
        offsprings = []

        for i in range(int(len(self.population)/2)):
            parent1 = parents.pop(random.randint(0,len(parents)-1))    
            parent2 = parents.pop(random.randint(0,len(parents)-1))    
            sons = parent1.crossover(parent2)
            offsprings.extend(sons)

        return offsprings

    def get_mutations(self):
        mutations = []
        for individual in self.population:
            aux_mutation = individual.mutate()
            mutations.append(aux_mutation)
        return mutations

    #Problems to select an random value with non-integer values
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

        #They will be the next population generation 
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

        #This function needs some corrections
    def elitism(self,elitism:int):
        elite = []

        for i in range(elitism):
            pop_index = 0
            best = self.population[0]
            for index in range(len(self.population)-1):
                if self.population[index].chromosome < best.chromosome:
                    best = self.population[index]
                    pop_index = index
            self.population.pop(pop_index)
            elite.append(best)
        return elite
           

    def printer(self, gen:int):
        best = self.population[0]
        for chromosome in self.population:
            if not self.maximization and chromosome.get_evaluate() <= best.get_evaluate():
                best = chromosome
            elif self.maximization and chromosome.get_evaluate() >= best.get_evaluate():
                best = chromosome
        print('Geração: {} Individuo: {} Avaliacao: {}'.format(gen,best.chromosome,best.avaliacao))
