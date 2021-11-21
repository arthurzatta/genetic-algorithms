import numpy as np
from numpy import ndarray
from math import exp
from interfaces.rna import RNA


class MLP(RNA):

    def __init__(self, qtd_in: int, qtd_h: int, qtd_out: int, dataset: ndarray, ages: int, min_value: float, max_value: float, ni: float):
        self.qtd_in = qtd_in
        self.qtd_out = qtd_out
        self.qtd_h = qtd_h
        self.dataset = dataset
        self.ages = ages
        self.min = min_value
        self.max = max_value
        self.weigth_hiden = self.weigth_matrix(self.qtd_in+1, self.qtd_h)
        self.weigth_theta = self.weigth_matrix(self.qtd_h+1, self.qtd_out)
        self.ni = ni

    def aproximation_error(self, expected_output: ndarray, sigmoid: ndarray):
        result = 0
        for i in range(expected_output.size):
            result += abs(expected_output[i] - sigmoid[i])
        return result

    def classification_error(self, expected_output: ndarray, output: ndarray):
        threshold_array = np.zeros(output.size)

        for sample in range(output.size):
            threshold_array[sample] = self.threshold(sample)

        aprox_error = self.aproximation_error(expected_output, threshold_array)

        if aprox_error > 0: 
            return 1
        return 0
        
    def sigmoid(self, value: float):
        return 1/(1 + exp(-value))
    
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

    def delta_h(self, hiden_array: ndarray, w_theta: ndarray, delta_theta: ndarray):
        delta_h = np.copy(hiden_array)
        # print(delta_h)
        # input()
        for h in range(len(delta_h)):
            summation = 0
            for j in range(delta_theta.size):
                summation += delta_theta[j] * w_theta[h][j]
            delta_h[h] = hiden_array[h] * (1-hiden_array[h]) * summation
        return delta_h

    def weigth_matrix(self, rows: int, columns: int):
        weigth_matrix = np.random.uniform(
            low=self.min, high=self.max, size=(rows, columns))
        return weigth_matrix

    def theta_weigth_adjustment(self, ni: float, delta_theta: ndarray, hiden_array: ndarray):
        for h in range(len(self.weigth_theta)):
            for j in range(len(self.weigth_theta[0])):
                self.weigth_theta[h][j] += ni * delta_theta[j] * hiden_array[h]

    def hiden_weigth_adjustment(self, delta_hiden: ndarray, ni: float, x_in: ndarray):
        for i in range(len(self.weigth_hiden)):
            for h in range(len(self.weigth_hiden[0])):
                self.weigth_hiden[i][h] += ni * delta_hiden[h] * x_in[i]

    def age_total_error(self, error: ndarray):
        result = 0.0
        for i in range(error.size):
            result += error[i]
        return result

    def printer(self, age: int, error: float):
        print('{} - {}'.format(age, error))

    def treinar(self, x_in: ndarray, y: ndarray) -> float:
        x = np.append(x_in, 1)

        # summation of the weigths from the hiden layer times the inputs
        H = np.zeros(self.qtd_h+1)
        for h in range(H.size-1):
            sum_result = 0
            for i in range(x.size):
                sum_result += x[i] * self.weigth_hiden[i][h]
            H[h] = self.sigmoid(sum_result)
        H[H.size-1] = 1

        output = np.zeros(self.qtd_out)

        for j in range(output.size):
            sum_result = 0
            for h in range(H.size):
                sum_result += H[h] * self.weigth_theta[h][j]
            output[j] = self.sigmoid(sum_result)

        delta_theta = self.delta_theta(output, y)
        delta_h = self.delta_h(H, self.weigth_theta, delta_theta)
        
        self.theta_weigth_adjustment(
            ni=self.ni, delta_theta=delta_theta, hiden_array=H)
        self.hiden_weigth_adjustment(delta_hiden=delta_h, ni=self.ni, x_in=x)

        return output

    def executar(self):

        # errors = np.zeros(len(self.dataset))
        errors = {
            "aproximation": np.zeros(len(self.dataset)),
            "classification": np.zeros(len(self.dataset))
        }

        for age in range(self.ages):
            for j in range(len(self.dataset)):

                x_in = self.dataset[j][:self.qtd_in]
                y = self.dataset[j][self.qtd_in:]

                output = self.treinar(x_in, y)
                aprx_error = self.aproximation_error(y, output)
                class_error = self.classification_error(y, output)

                errors["aproximation"][j] = aprx_error
                errors["classification"][j] = class_error
            
            total_error_aprox = self.age_total_error(errors["aproximation"])
            total_error_class = self.age_total_error(errors["classification"])
            self.printer(age=age, error=total_error_aprox)
