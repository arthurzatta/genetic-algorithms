from controller.runner import Runner
from model.perceptron import Perceptron
from utils.data_handling import balance_data_handling
from config import AGES, MAX_INTERVAL, MIN_INTERVAL, SAMPLE_PATH, SAMPLE_RESULT_PATH
import time
import numpy as np

if __name__ == "__main__":
    perceptron = Perceptron()

    sample = balance_data_handling(SAMPLE_PATH)
    time_start = time.time()

    print('Balance Scale')
    sample_result = Runner(dataset=sample,ages=AGES,min_value=MIN_INTERVAL,max_value=MAX_INTERVAL,n_out=3, perceptron=perceptron).executer()

    time_end = time.time()

    print('Tempo gasto: {}'.format((time_end - time_start)/60))

    