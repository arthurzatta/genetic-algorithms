import random
class Ag:
    def __init__(self):
        self.population = []
        self.maximization = False
        self.factory = None
        
    def initial_population(self, nInd: int, a:int, b:int, dimension: int):
        genes = lambda a,b: random.uniform(a,b)
        self.population = [self.factory([genes(a,b) for d in range(2)])  for i in range(nInd)]

    def execute(self,nGen:int,nInd:int,elitism:int,maximization:bool,interval: tuple, dimension:int ,factory) -> None:
        self.factory = factory
        self.initial_population(nInd, interval[0], interval[1], dimension)
        
        self.maximization = maximization
        
        for gen in range(nGen):
            aux_population = []
            
            aux_population.extend(self.population)
            aux_population.extend(self.get_recombinations(factory))
            aux_population.extend(self.get_mutations())        
            

            self.population = aux_population
            elite = self.elitism(elitism)

            self.selection(nInd-elitism)
            self.population.extend(elite)

            self.printer(gen)
     
    def get_recombinations(self,factory) -> list:
        offsprings = []

        for i in range(0,int(len(self.population)/2),2):
            parents = [self.population[i],self.population[i+1]]
            sons = parents[0].crossover(parents[1].chromosome)
            aux = [self.factory(i) for i in sons]
            offsprings.extend(aux)
        return offsprings 

    def get_mutations(self) -> list:
        return list(map(lambda individual: self.factory(individual.mutate()), self.population))

    def selection(self, nInd: int):
        selected_genes = []
        total = self.__evaluation_total() 

        aux = sorted(self.population, key=lambda i: i.fitness)
        for i in range(nInd):
            if self.maximization:
                random_sorted = random.randint(0,total)
            else:
                random_sorted = random.uniform(0,total) 
            value = self.__wheel_rotation(random_sorted, aux)
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
        
    def __wheel_rotation(self,raffled,aux):
        roulette_sum = 0
        selected = None

        for chromosome in aux:

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
        best = []

        if not self.maximization:
            best = sorted(self.population, key=lambda individual: individual.fitness)
        else:
            best = sorted(self.population, key=lambda individual: individual.fitness, reverse=True)
        print('Gera????o: \t{} Individuo: \t{} \tAvalia????o: {}'.format(gen,best[0].chromosome,best[0].fitness))
