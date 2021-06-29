import random
import math

class nQueens:
    
    def __init__(self, chromosome: list, n_rainhas=8):
        self.n_rainhas = n_rainhas
        self.chromosome = chromosome
        self.fitness = 0
        self.evaluated = False

    def crossover_second_part(self, chromosome:list, son:list):
        for i in chromosome[4:]:
            try:
                check = son.index(i)
                son.append(-1)
            except ValueError:
                son.append(i)
    
    def check(self, chromosome:list):
        check = []

        for i in range(len(chromosome)):
            try:
                chromosome.index(i)
            except ValueError:
                check.append(i)

        while len(check) != 0: 
            rand = random.randint(0,len(check)-1)
            index = chromosome.index(-1)
            checked_value = check.pop(rand)
            chromosome.pop(index)

            chromosome.insert(index, checked_value)

    def crossover(self, individual):
        son1 = self.chromosome[:4]
        son2 = individual.chromosome[:4]
        
        self.crossover_second_part(individual.chromosome, son1)
        self.crossover_second_part(self.chromosome, son2)
        
        self.check(son1)
        self.check(son2)

        return [nQueens(son1), nQueens(son2)] 

    def mutate(self, mutation_rate=0.05):
        mutation = self.chromosome.copy()
        aux_mutation = False
        
        for mutation_index in range(self.n_rainhas):
            random_rate = random.random()
            if random_rate >= mutation_rate:
               mutation = self.__swap(mutation, mutation_index)
               aux_mutation = True

        if not aux_mutation:
            rand_pos = random.randint(0,self.n_rainhas-1)
            mutation = self.swap(mutation, rand_pos)
        return nQueens(mutation)

    def __swap(self, mutant:list, mutation_index:int):
        new_chromosome = mutant[mutation_index] 
        
        while new_chromosome  == mutant[mutation_index]:
            new_chromosome = random.randint(0,self.n_rainhas-1)

        index = mutant.index(new_chromosome)
        mutant[index] = mutant[mutation_index] 
        mutant[mutation_index] = new_chromosome
        
        return mutant

    def evaluate(self):
        weigth = 0
        for i in range(self.n_rainhas):
            for j in range(i+1,self.n_rainhas):
                absolute = abs(j-i)
                if(self.chromosome[i] == self.chromosome[j] or self.chromosome[i] == self.chromosome[j] - absolute or self.chromosome[i] == self.chromosome[j] + absolute):
                    weigth += 1
        return weigth

    def get_evaluate(self):
        if not self.evaluated:
            self.fitness = self.evaluate()
            self.evaluated = True
        return  self.fitness


