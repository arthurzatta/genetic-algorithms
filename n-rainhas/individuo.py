from abc import ABC, abstractmethod

class Individuo(ABC):
    
    def __init__(self):
        self.avaliado = False
        self.avaliacao = 0
        super().__init__()

    #crossover
    @abstractmethod
    def crossover(self, individual):
        pass
    
    #mutations
    @abstractmethod
    def mutate(self):
        pass

    
    #fitness
    @abstractmethod
    def evaluate(self):
        pass

    def get_evaluate(self):
        if not self.avaliado:
            self.avaliacao = self.evaluate()
            self.avaliado = True
        return  self.avaliacao

    
