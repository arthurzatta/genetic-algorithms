from abc import ABC, abstractmethod

class Individuo(ABC):
    
    def __init__(self):
        self._avaliado = False
        self._avaliacao = 0.0

    #crossover
    @abstractmethod
    def recombinar(self, individuo):
        pass
    
    #mutations
    @abstractmethod
    def mutar(self):
        pass
    
    #fitness
    @abstractmethod
    def avaliar(self) -> float:
        pass

    def get_avaliacao(self):
        if not self._avaliado:
            self._avaliacao = self.avaliar()
        return  self._avaliacao

    
