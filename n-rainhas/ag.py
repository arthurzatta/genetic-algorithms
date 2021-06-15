from nRainhasFactory import RainhasFactory as factory 
import random

class AG:
    def __init__(self):
        self.population = []
    
    def initial_population(self, nInd: int):
        for individuo in range(nInd):
            auxGene = random.sample(list(range(8)), k=8)
            self.population.append(factory.rainhasFactory(auxGene))

    def executar(self, nGen: int, nInd: int):
        self.initial_population(nInd)
        self.population.extend(self.get_filhos())

    #Maybe can be made better
    def get_filhos(self):
        parents = self.population.copy()
        offsprings = []

        for i in range(int(len(self.population)/2)):
            parent1 = parents.pop(random.randint(0,len(parents)-1))    
            parent2 = parents.pop(random.randint(0,len(parents)-1))    
            sons = parent1.recombinar(parent2)
            offsprings.extend(sons)

        return offsprings

    def get_mutations(self):
        pass

if __name__ == "__main__":
    ag = AG()
    sons = ag.executar(4000, 5)
    print(sons)