from individuo import Individuo

class nRainhasInd(Individuo):
    
    def __init__(self, genes: list, nRainhas=8):
        self.nRainhas = nRainhas
        self.genes = genes

    #Pares de cromossomos se recombinam entre si
    def recombinar(self, p2):
        son1 = self.genes[:4]
        son1.append(p2.genes[4:])

        son2 = p2.genes[:4]
        son2.append(self.genes[4:])

        return [nRainhasInd(son1), nRainhasInd(son2)]

    def mutar(self):
        pass
    
    #O fitness vai ser feito avaliando o numero de colisoes para cada individuo
    #Usando vetores as colisoes verticais são eliminadas 
    def avaliar(self):
        pass

