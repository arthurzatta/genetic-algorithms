from .surjano import Surjano
from math import pow

class Dixon(Surjano):
    def __init__(self, chromosome):
        super().__init__(chromosome)

    def evaluate(self) -> float:
        dimension = len(self.chromosome)-1
        result = 0
        first_term = self.chromosome[0]
        # xi = list(map(lambda i: 2 ** (-((2 ** i)-2)/(2 ** i)), [1,2]))
        
        for i in range(1, dimension):
            result += i * ((2 * (self.chromosome[i] ** 2) - self.chromosome[i-1]) ** 2)
        return (first_term - 1) ** 2 + result