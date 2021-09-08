from math import exp
from numpy import ndarray


class Perceptron:

    def summation(self, dataset: ndarray, weigth_values: ndarray):
        result = 0
        for i in range(dataset.size):
            result += dataset[i] * weigth_values[i]
        return result

    def sigmoidal(self, value: float):
        return 1/(1 + exp(-value))

    def error(self, expected_value: float, sigm: float):
        return abs(expected_value - sigm)

    def new_weigth(self, expected_value: float,sigm: float, xi: float, weigth: float):
        return weigth + (0.3 * (expected_value - sigm) * xi)
