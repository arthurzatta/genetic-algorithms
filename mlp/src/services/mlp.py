import numpy as np
from interfaces.rna import RNA


class MLP(RNA):
    def __init__(self, qtd_in: int, qtd_h: int, qtd_out: int, dataset: np.ndarray):
      self.qtd_in = qtd_in
      self.qtd_out = qtd_out
      self.qtd_h = qtd_h
      self.dataset = dataset

    def aproximation_error(self, expected_output: float, sigmoid: float):
      return abs(expected_output - sigmoid)

    # def sigmoid(self,)

    def hiden_layer(self):
      weigths_matrix = np.random.uniform(low=-0.3, high=0.3,size=(self.qtd_in+1,self.qtd_h)) 
      for column in range(self.qtd_h):
        weigths_matrix[self.qtd_in][column] = 1 
      return weigths_matrix

    def output_layer(self):
      weigths_matrix = np.random.uniform(low=-0.3, high=0.3,size=(self.qtd_h+1,self.qtd_out)) 
      for column in range(self.qtd_out):
        weigths_matrix[self.qtd_h][column] = 1 
      return weigths_matrix



    def treinar(self, x_in: np.ndarray, y: np.ndarray):
      hiden_layer = self.hiden_layer()
      print(hiden_layer)

      #entries array
      #x_in = [x0 x1 bias]
      x_in = np.append(x_in, 1)
      
      #array of results from w*x
      #H = [(w00*x0+w10*x1) (w01*x0+w11*x1) bias]
      H = np.ones(self.qtd_h+1)

      for j in range(self.qtd_h):
        aux = 0
        for i in range(self.qtd_in):
          aux += x_in[i] * hiden_layer[i][j]
        H[j] = aux

      print(H)        


    def executar(self):

      x_in = self.dataset[0][:self.qtd_in]
      y = self.dataset[0][self.qtd_in:]
      
      self.treinar(x_in, y)