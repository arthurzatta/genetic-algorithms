import numpy as np
from numpy import ndarray
from math import exp
from interfaces.rna import RNA


class MLP(RNA):

    def __init__(self, qtd_in: int, qtd_h: int, qtd_out: int, dataset: dict, ages: int, min_value: float, max_value: float, ni: float):
        self.qtd_in = qtd_in
        self.qtd_out = qtd_out
        self.qtd_h = qtd_h
        self.dataset = dataset
        self.ages = ages
        self.min = min_value
        self.max = max_value
        self.weigth_hidden = self.weigth_matrix(self.qtd_in+1, self.qtd_h)
        self.weigth_theta = self.weigth_matrix(self.qtd_h+1, self.qtd_out)
        self.ni = ni

    def aproximation_error(self, expected_output: ndarray, sigmoid: ndarray):
        result = 0
        for i in range(len(expected_output)):
            result += abs(expected_output[i] - sigmoid[i])
        return result

    def classification_error(self, expected_output: ndarray, output: ndarray):
        threshold_array = np.zeros(output.size)

        for sample in range(output.size):
            threshold_array[sample] = self.threshold(output[sample])

        aprox_error = self.aproximation_error(expected_output, threshold_array)

        if aprox_error > 0: 
            return 1
        return 0
        
    def sigmoid(self, value: float):
        return 1/(1 + np.exp(-value))
    
    def threshold(self, theta: float):
        if theta >= 0.5: 
            return 1
        return 0

    def delta_theta(self, theta_array: ndarray, expected_output: ndarray) -> ndarray:
        delta_theta = np.copy(theta_array)
        for i in range(theta_array.size):
            theta = theta_array[i]
            delta_theta[i] = theta * (1-theta) * (expected_output[i] - theta)
        return delta_theta

    def delta_h(self, hidden_array: ndarray, w_theta: ndarray, delta_theta: ndarray):
        delta_h = np.copy(hidden_array)
        for h in range(len(delta_h)):
            summation = 0
            for j in range(delta_theta.size):
                summation += delta_theta[j] * w_theta[h][j]
            delta_h[h] = hidden_array[h] * (1-hidden_array[h]) * summation
        return delta_h

    def weigth_matrix(self, rows: int, columns: int):
        weigth_matrix = np.random.uniform(
            low=self.min, high=self.max, size=(rows, columns))
        return weigth_matrix

    def theta_weigth_adjustment(self, ni: float, delta_theta: ndarray, hidden_array: ndarray):
        for h in range(len(self.weigth_theta)):
            for j in range(len(self.weigth_theta[0])):
                self.weigth_theta[h][j] += ni * delta_theta[j] * hidden_array[h]

    def hidden_weigth_adjustment(self, delta_hidden: ndarray, ni: float, x_in: ndarray):
        for i in range(len(self.weigth_hidden)):
            for h in range(len(self.weigth_hidden[0])):
                self.weigth_hidden[i][h] += ni * delta_hidden[h] * x_in[i]

    def printer(self, epoch: int, training_aproximation_error: float, training_classification_error: float, test_aproximation_error: float, teste_classification_error: float):
        print('Época: {} - erroTreino de aproximação: {} - erroTreino de classificação: {} -  erroTeste de aproximação: {} -  erroTeste de classificação: {} '.format(epoch, training_aproximation_error, training_classification_error, test_aproximation_error, teste_classification_error))
    
    def treinar(self, x_in: ndarray, y: ndarray) -> float:
        layers = self.executar(x_in)

        output = layers['output_layer']
        H = layers['hidden_layer']

        delta_theta = self.delta_theta(output, y)
        delta_h = self.delta_h(H, self.weigth_theta, delta_theta)

        self.theta_weigth_adjustment(
            ni=self.ni, delta_theta=delta_theta, hidden_array=H)
        self.hidden_weigth_adjustment(delta_hidden=delta_h, ni=self.ni, x_in=x_in)

        return output

    def executar(self, x_in: ndarray) -> dict:
        H = np.zeros(self.qtd_h+1)
        for h in range(H.size-1):
            sum_result = 0
            for i in range(x_in.size):
                sum_result += x_in[i] * self.weigth_hidden[i][h]
            H[h] = self.sigmoid(sum_result)
        H[H.size-1] = 1

        output = np.zeros(self.qtd_out)
        for j in range(output.size):
            sum_result = 0
            for h in range(H.size):
                sum_result += H[h] * self.weigth_theta[h][j]
            output[j] = self.sigmoid(sum_result)
        
        return {"hidden_layer": H, "output_layer": output}

    def runner(self):
        for age in range(self.ages):
            training_error_epoch_aprox = 0
            training_error_epoch_class = 0

            test_error_epoch_aprox = 0
            test_error_epoch_class = 0

            for j in range(len(self.dataset)):

                x_in = np.append(self.dataset['training'][j][:self.qtd_in], 1)
                y = self.dataset['training'][j][self.qtd_in:]

                output = self.treinar(x_in, y)
                training_error_sample_aprox = self.aproximation_error(y, output)
                training_error_sample_class = self.classification_error(y, output)

                training_error_epoch_aprox += training_error_sample_aprox
                training_error_epoch_class += training_error_sample_class

                x2_in = np.append(self.dataset['test'][j][:self.qtd_in], 1)
                y2 = self.dataset['test'][j][self.qtd_in:]

                output = self.executar(x2_in)['output_layer']
                test_error_sample_aprox = self.aproximation_error(y2, output)
                test_error_sample_class = self.classification_error(y2, output)

                test_error_epoch_aprox += test_error_sample_aprox
                test_error_epoch_class += test_error_sample_class

            self.printer(epoch=age, training_aproximation_error=training_error_epoch_aprox, training_classification_error=training_error_epoch_class, test_aproximation_error=test_error_epoch_aprox, teste_classification_error=test_error_epoch_class)
            