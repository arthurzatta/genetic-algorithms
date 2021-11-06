import numpy as np
from numpy import ndarray
from math import exp
from interfaces.rna import RNA


class MLP(RNA):
    def __init__(self, qtd_in: int, qtd_h: int, qtd_out: int, dataset: ndarray, ages: int, min_value: float, max_value: float):
        self.qtd_in = qtd_in
        self.qtd_out = qtd_out
        self.qtd_h = qtd_h
        self.dataset = dataset
        self.ages = ages
        self.min = min_value
        self.max = max_value
        self.output_layer = self.weigths_matrix(self.qtd_h+1, self.qtd_out)
        self.hiden_layer = self.weigths_matrix(self.qtd_in+1, self.qtd_h)

    def aproximation_error(self, expected_output: ndarray, sigmoid: ndarray):
        result = 0
        for i in range(expected_output.size):
            result += abs(expected_output[i] - sigmoid[i])
        return result

    def sigmoid(self, value: float):
        return 1/(1 + exp(-value))

    def delta_sigmoid(self, theta_array: ndarray, expected_output: ndarray) -> ndarray:
        delta_theta = np.copy(theta_array)
        for i in range(theta_array.size):
            theta = theta_array[i]
            delta_theta[i] = theta * (1-theta) * (expected_output[i] - theta)
        return delta_theta

    def delta_h(self, hiden_array: ndarray, w_theta: ndarray, delta_theta: ndarray):
        delta_h = np.copy(hiden_array)
        for h in range(hiden_array.size):
            summation = 0
            for j in range(delta_theta.size):
                summation += delta_theta[j] * w_theta[h][j]
            delta_h[j] = hiden_array[h] * (1-hiden_array[h]) * summation
        return delta_h

    def weigths_matrix(self, rows: int, columns: int):
        weigths_matrix = np.random.uniform(
            low=self.min, high=self.max, size=(rows, columns))
        return weigths_matrix

    def theta_weigth_adjustment(self, w_theta: ndarray, ni: float, delta_theta: ndarray, hiden_array: ndarray):
        for h in range(len(w_theta)):
            for j in range(delta_theta.size):
                w_theta[h][j] += ni * delta_theta[j] * hiden_array[h]
        return w_theta

    def hiden_weigth_adjustment(self, w_hiden: ndarray, delta_hiden: ndarray, ni: float, x_in: ndarray):
        for i in range(x_in.size):
            for h in range(delta_hiden.size-1):
                w_hiden[i][h] += ni * delta_hiden[h] * x_in[i]
        return w_hiden

    def age_total_error(self, error: ndarray):
        result = 0.0
        for i in range(error.size):
            result += error[i]
        return result

    def printer(self, age: int, error: float):
        print('{} - {}'.format(age, error))

    def treinar(self, x_in: ndarray, y: ndarray):
        # hiden_layer = self.weigths_matrix(self.qtd_in+1,self.qtd_h)
        x_in = np.append(x_in, 1)

        # summation of the weigths from the hiden layer times the inputs
        H = np.ones(self.qtd_h+1)
        for j in range(self.qtd_h):
            sum_result = 0
            for i in range(self.qtd_in+1):
                sum_result += x_in[i] * self.hiden_layer[i][j]
            H[j] = self.sigmoid(sum_result)

        # output_layer = self.weigths_matrix(self.qtd_h+1,self.qtd_out)
        output = np.zeros(self.qtd_out)
        for j in range(self.qtd_out):
            sum_result = 0
            for i in range(H.size):
                sum_result += H[i] * self.output_layer[i][j]
            output[j] = self.sigmoid(sum_result)

        error = self.aproximation_error(y, output)

        delta_theta = self.delta_sigmoid(output, y)
        delta_h = self.delta_h(H, self.hiden_layer, delta_theta)

        self.hiden_layer = self.hiden_weigth_adjustment(
            self.hiden_layer, delta_h, 0.3, x_in)
        self.output_layer = self.theta_weigth_adjustment(
            self.output_layer, 0.3, delta_theta, H)

        return error

    def executar(self):

        for age in range(self.ages):

            errors = np.asarray([])

            for j in range(len(self.dataset)):

                x_in = self.dataset[j][:self.qtd_in]
                y = self.dataset[j][self.qtd_in:]

                error = self.treinar(x_in, y)
                errors = np.append(errors, [error])

            total_error = self.age_total_error(errors)
            self.printer(age=age, error=total_error)
