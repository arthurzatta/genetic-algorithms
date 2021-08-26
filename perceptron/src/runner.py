import numpy as np
from numpy import ndarray
from perceptron import Perceptron


class Runner:
    def __init__(self, dataset: ndarray, ages: int, min_value: float, max_value: float, perceptron: Perceptron):
        self.dataset = dataset
        self.min = min_value
        self.max = max_value
        self.ages = ages
        self.__weights = []
        self.perceptron = perceptron
        self.errors = []

    def executer(self):

        length = self.dataset[0].size

        self.__weights = np.random.uniform(low=self.min, high=self.max, size=(length))
        
        for age in range(self.ages):

            errors = np.asarray([])

            for j in range(length):
                #Cada amostra recebe x0 = 1 ou x[0] = 1
                sample_array = np.append([1], self.dataset[j])
                error = self.runner_sample(sample_array)
                errors = np.append(errors, [error])

            total_error = self.age_total_error(errors)
            self.printer(age=age, error=total_error)   

    def runner_sample(self, dataset_row: ndarray):

        idx = dataset_row.size-1
        expected_result = dataset_row[idx]

        # Somatorio
        summation = self.perceptron.summation(dataset_row[:idx], self.__weights)

        # Sigmoidal
        sigm = self.perceptron.sigmoidal(summation)

        # Error
        error = self.perceptron.error(expected_result, sigm)

        # Novos pesos
        for i in range(self.__weights.size):
            self.__weights[i] = self.perceptron.new_weigth(
                expected_value=expected_result,
                sigm=sigm,
                xi=dataset_row[i],
                weigth=self.__weights[i]
            )

        return error

    def age_total_error(self, error: ndarray):
        result = 0.0
        for i in range(error.size):
            result += error[i]
        return result

    def printer(self, age: int, error: float):
        print('{} - {}'.format(age, error))
