from individuo import Individuo
import random
import math

class nRainhasInd(Individuo):
    
    def __init__(self, genes: list, n_rainhas=8):
        self.n_rainhas = n_rainhas
        self.genes = genes

    #Horizontal collisions needs to be considered
    def crossover(self, p2):
        son1 = self.genes[:4]
        son2 = p2.genes[:4]
        
        son1 = self.crossover_second_part(p2, son1)
        son2 = self.crossover_second_part(self.genes, son2)

        for i in range(8):
            try:
                check = son1.
        

        return [nRainhasInd(son1), nRainhasInd(son2)] 

    def crossover_second_part(self, genes:list, son:list):
        for i in genes[4:]:
            try:
                check = son.index(i)
                son.append(-1)
            except ValueError:
                son.append(i)
        return son



    '''
        Mutation rate based in a percent of 0 to 1
        Compare each chromosome of an individual if it is less than mutation rate
        the individual needs to mutate that chromosome.
        If none of the chromosomes satisfy this condition, one of them needs to be randomly selected and changed.
    '''
    def mutate(self, mutation_rate=0.05):
        mutation = self.genes.copy()
        aux_mutation = False

        for pos in range(len(self.genes)):
            rand_value = random.random()
            if rand_value >= mutation_rate:
               mutation = self.swap(mutation, pos)
               aux_mutation = True

        #In case of any chromosome has been changed by the mutation rate, one of them will be randomly choose 
        if not aux_mutation:
            rand_pos = random.randint(0,8)
            mutation = self.swap(mutation, rand_pos)
        return mutation

    def swap(self,mutant, pos):
        new_chromosome = mutant[pos] 
        while new_chromosome == mutant[pos]:
            new_chromosome = random.randint(0,8)
        index = mutant.index(new_chromosome)
        mutant.insert(index, mutant[pos])
        mutant.insert(pos, new_chromosome)   

        return new_chromosome

    #The fitness is the evaluation of number collisions of each queen.
    def evaluate(self):
        weigth = 0
        for i in range(self.n_rainhas):
            for j in range(i+1,self.n_rainhas):
                abs = math.fabs(j-i)
                if(self.genes[i] == self.genes[j] or self.genes[i] == self.genes[j] - abs or self.genes[i] == self.genes[j] + abs):
                    weigth += 1
        return weigth
