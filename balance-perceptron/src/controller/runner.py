import numpy as np
from numpy import ndarray
from model.perceptron import Perceptron

class Runner:
    def __init__(self, dataset: ndarray, ages: int, min_value: float, max_value: float, n_out:int, perceptron: Perceptron):
        self.dataset = np.asarray(dataset)
        self.min = min_value
        self.max = max_value
        self.ages = ages
        self.__weights = []
        self.perceptron = perceptron
        self.n_out = n_out
        self.errors = []

    def executer(self):

        idx = self.dataset[0].size - self.n_out

        #Gera a matriz de pesos
        self.__weights = np.random.uniform(low=self.min, high=self.max, size=(self.n_out, idx+1))
        
        for age in range(self.ages):

            errors = np.asarray([])

            for j in range(len(self.dataset)):

                expected_results = self.dataset[j][idx:]
                
                x_in = np.append([1], self.dataset[j][:idx])
                error_result = self.runner_sample(x_in, expected_results)
                errors = np.append(errors, error_result)

            total_error = self.age_total_error(errors)
            self.printer(age=age, error=total_error)   

    def runner_sample(self, dataset_row: ndarray,  expected_results: ndarray) -> ndarray:

        errors = []

        for i in range(expected_results.size):
            #Somatorio
            summation = self.perceptron.summation(dataset_row, self.__weights[i])

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
        result = 0
        for i in range(error.size):
            result += error[i]
        return result

    def printer(self, age: int, error: float):
        print('{} - {}'.format(age, error))
