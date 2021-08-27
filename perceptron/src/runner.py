import numpy as np
from numpy import ndarray
from perceptron import Perceptron


class Runner:
    def __init__(self, dataset: ndarray, ages: int, min_value: float, max_value: float, n_out:int, perceptron: Perceptron):
        self.dataset = dataset
        self.min = min_value
        self.max = max_value
        self.ages = ages
        self.__weights = []
        self.perceptron = perceptron
        self.n_out = n_out
        self.errors = []

    def executer(self):

        length = self.dataset[0].size

        #Gera a matriz de pesos
        self.__weights = np.random.uniform(low=self.min, high=self.max, size=(self.n_out, length))
        
        for age in range(self.ages):

            errors = np.asarray([])

            for j in range(len(self.dataset)):
                sample_array = np.append([1], self.dataset[j])
                error = self.runner_sample(sample_array)
                errors = np.append(errors, error)

            total_error = self.age_total_error(errors)
            self.printer(age=age, error=total_error)   

    def runner_sample(self, dataset_row: ndarray) -> ndarray:

        idx = dataset_row.size-self.n_out

        #Array de resultados
        expected_results = dataset_row[idx:]
        errors = []

        for i in range(expected_results.size):
            # print(self.__weights[i])
            #Somatorio
            summation = self.perceptron.summation(dataset_row[:idx], self.__weights[i])

            # Sigmoidal
            sigm = self.perceptron.sigmoidal(summation)

            # Error
            errors.append(self.perceptron.error(expected_results[i], sigm))

            # Novos pesos
            for j in range(self.__weights[i].size):
                self.__weights[i][j] = self.perceptron.new_weigth(
                    expected_value=expected_results[i],
                    sigm=sigm,
                    xi=dataset_row[j],
                    weigth=self.__weights[i][j]
                )
 
        return np.asarray(errors)

    def age_total_error(self, error: ndarray):
        result = 0.0
        for i in range(error.size):
            result += error[i]
        return result

    def printer(self, age: int, error: float):
        print('{} - {}'.format(age, error))
