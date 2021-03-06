from math import pow
from .surjano import Surjano

class RotatedEllipsoid(Surjano):
    def __init__(self, chromosome):
        super().__init__(chromosome)
    
    def evaluate(self) -> float:
        dimension = len(self.chromosome)
        result = 0
        for i in range(dimension):
            result += (dimension-i) * pow(self.chromosome[i],2)
        return result
